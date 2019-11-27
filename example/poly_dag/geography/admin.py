from django.contrib import admin
from django.contrib.auth import get_user_model

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from poly_dag.geography.models import WorldBorder, BaseGeoNode, GeoPumpNode, GeoCanalNode, BaseGeoEdge



User = get_user_model()


@admin.register(WorldBorder)
class WorldBorderAdmin(admin.ModelAdmin):

    # fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["name", "lon", "lat", "mpoly"]
    search_fields = ["name"]


class BaseGeoNodeChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = BaseGeoNode  # Optional, explicitly set here.

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    # base_form = ...
    # base_fieldsets = (
    #     ...
    # )


@admin.register(GeoPumpNode)
class GeoPumpNodeAdmin(BaseGeoNodeChildAdmin):
    base_model = GeoPumpNode  # Explicitly set here!
    show_in_index = True
    # define custom features here


@admin.register(GeoCanalNode)
class GeoCanalNodeAdmin(BaseGeoNodeChildAdmin):
    base_model = GeoCanalNode  # Explicitly set here!
    show_in_index = True
    # define custom features here


@admin.register(BaseGeoNode)
class BaseGeoNodeParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = BaseGeoNode  # Optional, explicitly set here.
    child_models = (GeoPumpNode, GeoCanalNode)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.