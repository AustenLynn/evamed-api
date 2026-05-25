from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

from projects_api import models
from projects_api import serializers
from profiles_api import permissions

class UserPlatformViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user"""
    serializer_class = serializers.UserPlatformSerializer
    queryset = models.UserPlatform.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=email', )

class TransportsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating transports"""
    serializer_class = serializers.TransportsSerializer
    queryset = models.Transport.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class UsesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating uses"""
    serializer_class = serializers.UsesSerializer
    queryset = models.Use.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_use', )

class TypeProjectsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating type projects"""
    serializer_class = serializers.TypeProjectsSerializer
    queryset = models.TypeProject.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_type_project', )

class CountriesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating countries"""
    serializer_class = serializers.CountriesSerializer
    queryset = models.Country.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_country', )

class ExternalDistanceViewSet(viewsets.ModelViewSet):
    """Handle creating and updating countries"""
    serializer_class = serializers.ExternalDistanceSerializer
    queryset = models.ExternalDistance.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class UsefulLifeViewSet(viewsets.ModelViewSet):
    """Handle creating and updating useful life"""
    serializer_class = serializers.UsefulLifeSerializer
    queryset = models.UsefulLife.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_useful_life', )

class HousingSchemeViewSet(viewsets.ModelViewSet):
    """Handle creating and updating housing Scheme"""
    serializer_class = serializers.HousingSchemeSerializer
    queryset = models.HousingScheme.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_housing_scheme', )

class ProjectsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.ProjectsSerializer
    queryset = models.Project.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id',)

class MaterialsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating materials"""
    serializer_class = serializers.MaterialsSerializer
    queryset = models.Material.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['=id', 'name_material']

class SectionsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating sections"""
    serializer_class = serializers.SectionsSerializer
    queryset = models.Section.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_section', )

class OriginsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating origins"""
    serializer_class = serializers.OriginsSerializer
    queryset = models.Origin.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_origin', )

class UnitsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating units"""
    serializer_class = serializers.UnitsSerializer
    queryset = models.Unit.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_unit', )

class StandardsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating standards"""
    serializer_class = serializers.StandardsSerializer
    queryset = models.Standard.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_standard', )

class PotentialTypesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating potential types"""
    serializer_class = serializers.PotentialTypesSerializer
    queryset = models.PotentialType.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_potential_type', )

class VolumeUnitsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating volume units"""
    serializer_class = serializers.VolumeUnitsSerializer
    queryset = models.VolumeUnit.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_volume_unit', )

class EnergyUnitsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating energy units"""
    serializer_class = serializers.EnergyUnitsSerializer
    queryset = models.EnergyUnit.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_energy_unit', )

class BulkUnitsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating bulk units"""
    serializer_class = serializers.BulkUnitsSerializer
    queryset = models.BulkUnit.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_bulk_unit', )

class SourceInformationViewSet(viewsets.ModelViewSet):
    """Handle creating and updating source information"""
    serializer_class = serializers.SourceInformationSerializer
    queryset = models.SourceInformation.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_source_information', )

class ConstructiveProcessViewSet(viewsets.ModelViewSet):
    """Handle creating and updating source information"""
    serializer_class = serializers.ConstructiveProcessSerializer
    queryset = models.ConstructiveProcess.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_constructive_process', )

class MaterialSchemeProjectViewSet(viewsets.ModelViewSet):
    """Handle creating and updating material scheme project"""
    serializer_class = serializers.MaterialSchemeProjectSerializer
    queryset = models.MaterialSchemeProject.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=material_id', )

class MaterialSchemeProjectOriginalViewSet(viewsets.ModelViewSet):
    """Handle creating and updating material scheme project"""
    serializer_class = serializers.MaterialSchemeProjectOriginalSerializer
    queryset = models.MaterialSchemeProjectOrigianal.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=material_id', )

class MaterialSchemeDataViewSet(viewsets.ModelViewSet):
    """Handle creating and updating material scheme data"""
    serializer_class = serializers.MaterialSchemeDataSerializer
    queryset = models.MaterialSchemeData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('value', )

class ConstructiveSystemElementViewSet(viewsets.ModelViewSet):
    """Handle creating and updating CSE"""
    serializer_class = serializers.ConstructiveSystemElementSerializer
    queryset = models.ConstructiveSystemElement.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=project_id', )


class MaterialStageView(APIView):
    """Handle materials-stage checkbox options"""

    def get(self, request):
        project_id = request.query_params.get('project_id')
        if project_id is None:
            return Response(
                {'detail': 'project_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        queryset = models.MaterialStageSystemSelection.objects.filter(
            project_id_id=project_id
        )
        section_id = request.query_params.get('section_id')
        if section_id is not None:
            queryset = queryset.filter(section_id_id=section_id)

        queryset = queryset.order_by('section_id_id', 'origin_id_id', 'construction_system')
        data = serializers.MaterialStageSystemSelectionSerializer(queryset, many=True).data
        return Response({'items': data}, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request):
        payload = serializers.MaterialStageSelectionUpsertSerializer(data=request.data)
        payload.is_valid(raise_exception=True)
        validated = payload.validated_data

        project_id = validated['project_id']
        if not models.Project.objects.filter(id=project_id).exists():
            return Response(
                {'detail': 'Invalid project_id'},
                status=status.HTTP_400_BAD_REQUEST
            )

        results = []
        for item in validated['items']:
            section_id = item['section_id']
            origin_id = item.get('origin_id')
            has_is_selected = 'is_selected' in item

            if not models.Section.objects.filter(id=section_id).exists():
                return Response(
                    {'detail': f'Invalid section_id: {section_id}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if origin_id is not None and not models.Origin.objects.filter(id=origin_id).exists():
                return Response(
                    {'detail': f'Invalid origin_id: {origin_id}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if has_is_selected:
                selection, _ = models.MaterialStageSystemSelection.objects.update_or_create(
                    project_id_id=project_id,
                    section_id_id=section_id,
                    origin_id_id=origin_id,
                    construction_system=item['label'],
                    defaults={'is_selected': item['is_selected']}
                )
            else:
                selection, _ = models.MaterialStageSystemSelection.objects.get_or_create(
                    project_id_id=project_id,
                    section_id_id=section_id,
                    origin_id_id=origin_id,
                    construction_system=item['label']
                )

            results.append(selection)

        data = serializers.MaterialStageSystemSelectionSerializer(results, many=True).data
        return Response({'items': data}, status=status.HTTP_200_OK)


class MaterialStageUpdateView(APIView):
    """Update materials-stage checkbox state"""

    @transaction.atomic
    def patch(self, request):
        return self._update_selection_state(request)

    @transaction.atomic
    def post(self, request):
        return self._update_selection_state(request)

    def _update_selection_state(self, request):
        payload = serializers.MaterialStageSelectionUpdateSerializer(data=request.data)
        payload.is_valid(raise_exception=True)
        validated = payload.validated_data

        project_id = validated['project_id']
        if not models.Project.objects.filter(id=project_id).exists():
            return Response(
                {'detail': 'Invalid project_id'},
                status=status.HTTP_400_BAD_REQUEST
            )

        item_updates = validated.get('items', [])
        selected_ids = validated.get('selectedIds', [])
        unselected_ids = validated.get('unselectedIds', [])

        if selected_ids:
            item_updates.extend([
                {'sistemaConstructivoId': item_id, 'is_selected': True}
                for item_id in selected_ids
            ])
        if unselected_ids:
            item_updates.extend([
                {'sistemaConstructivoId': item_id, 'is_selected': False}
                for item_id in unselected_ids
            ])

        updated_ids = []
        for item in item_updates:
            selection_id = item['sistemaConstructivoId']
            selection = models.MaterialStageSystemSelection.objects.filter(
                id=selection_id,
                project_id_id=project_id
            ).first()
            if selection is None:
                return Response(
                    {'detail': f'Invalid sistemaConstructivoId: {selection_id}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            selection.is_selected = item['is_selected']
            selection.save(update_fields=['is_selected'])
            updated_ids.append(selection.id)

        queryset = models.MaterialStageSystemSelection.objects.filter(
            id__in=updated_ids
        ).order_by('id')
        data = serializers.MaterialStageSystemSelectionSerializer(queryset, many=True).data
        return Response({'items': data}, status=status.HTTP_200_OK)

class SourcesElectricityConsumptionViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create source electricity consumption"""
    serializer_class = serializers.SourcesElectricityConsumptionSerializer
    queryset = models.SourcesElectricityConsumption.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_source_electricity_consumption', )

class AnnualConsumptionRequiredViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create ACR"""
    serializer_class = serializers.AnnualConsumptionRequiredSerializer
    queryset = models.AnnualConsumptionRequired.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=project_id', )

class ElectricityConsumptionDataViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create ECD"""
    serializer_class = serializers.ElectricityConsumptionDataSerializer
    queryset = models.ElectricityConsumptionData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=annual_consumption_required_id', )

class StageSchemeDataViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create SSD"""
    serializer_class = serializers.StageSchemeDataSerializer
    queryset = models.StageSchemeData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class TypeEnergyViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create TypeEnergy"""
    serializer_class = serializers.TypeEnergySerializer
    queryset = models.TypeEnergy.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class ElectricityConsumptionDeconstructiveProcessViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create ECDP"""
    serializer_class = serializers.ElectricityConsumptionDeconstructiveProcessSerializer
    queryset = models.ElectricityConsumptionDeconstructiveProcess.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class TreatmentOfGeneratedWasteViewSet(viewsets.ModelViewSet):
    """Handle creating and updating create TOGW"""
    serializer_class = serializers.TreatmentOfGeneratedWasteSerializer
    queryset = models.TreatmentOfGeneratedWaste.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class SourceInformationDataViewSet(viewsets.ModelViewSet):
    """Handle creating and updating Source information data"""
    serializer_class = serializers.SourceInformationDataSerializer
    queryset = models.SourceInformationData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('value', )

class TypeEnergyDataViewSet(viewsets.ModelViewSet):
    """Handle creating and updating Type Energy Data"""
    serializer_class = serializers.TypeEnergyDataSerializer
    queryset = models.TypeEnergyData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('value', )

class StatesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating states"""
    serializer_class = serializers.StatesSerializer
    queryset = models.State.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class CitiesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating cities"""
    serializer_class = serializers.CitiesSerializer
    queryset = models.City.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class LocalDistancesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating local distances"""
    serializer_class = serializers.LocalDistancesSerializer
    queryset = models.LocalDistance.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class PotentialTransportViewSet(viewsets.ModelViewSet):
    """Handle creating and updating potential transports"""
    serializer_class = serializers.PotentialTransportSerializer
    queryset = models.PotentialTransport.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class ConversionsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating conversions"""
    serializer_class = serializers.ConversionsSerializer
    queryset = models.Conversions.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )

class DataBaseMaterialViewSet(viewsets.ModelViewSet):
    """Handle creating and updating DataBaseMaterial"""
    serializer_class = serializers.DataBaseMaterialSerializer
    queryset = models.DataBaseMaterial.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=id', )
