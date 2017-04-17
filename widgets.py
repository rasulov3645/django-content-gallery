import os

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from . import utils
from . import settings

class ContentTypeSelect(forms.Select):

    def _filter_choices(self):
        filtered_choices = []
        for choice in self.choices:
            try:
                if choice[0] == "":
                    filtered_choices.append(choice)
                    continue
                ctype = ContentType.objects.get(pk=int(choice[0]))
                model_class = ctype.model_class()
                if model_class.gallery_visible:
                    filtered_choices.append(choice)
            except:
                pass
        self.choices = filtered_choices

    def render(self, name, value, attrs=None):
        self._filter_choices()
        output = super().render(name, value, attrs)
        js = '''<script type="text/javascript">
            (function($) {
                $(function() {
                    $("#id_content_type").change(function() {
                        $("#id_object_id option:gt(0)").remove();
                        if (!this.value) return
                        $.ajax({
                            url: "%s" + this.value,
                            dataType: "json",
                            success: function (result) {
                                var $el = $("#id_object_id");
                                $.each(result, function (i, product) {
                                    $el.append($("<option></option>")
                                        .attr("value", product.id)
                                        .text(product.name));
                                });
                            }
                        });
                    });
                });
            })(django.jQuery);
        </script>'''
        output += js % utils.get_choices_url_pattern()
        return mark_safe(output)


class ObjectIdSelect(forms.Select):

    def _create_choices(self):
        choices = [("", "---------")]
        if self.model_class:
            items = self.model_class.objects.all()
            for item in items:
                choices.append((str(item.id), item))
        self.choices = choices

    def render(self, name, value, attrs=None):
        self._create_choices()
        return super().render(name, value, attrs)


class ImageWidget(forms.Widget):
    template_name = 'gallery/edit_inline/image_widget.html'

    def render(self, name, value, attrs=None):
        if value:
            img_url = value.image_url
        else:
            img_url = ""
        context = {
            "name": name,
            "value": value,
            "width": settings.GALLERY_THUMBNAIL_WIDTH,
            "height": settings.GALLERY_THUMBNAIL_HEIGHT,
            "img_url": img_url
        }
        return render_to_string(self.template_name, context)
