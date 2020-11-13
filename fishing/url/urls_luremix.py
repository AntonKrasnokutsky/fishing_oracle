from django.urls import path
from fishing.view import views_luremix


urlpatterns = [
    # Прикормочная смесь
    # Список прикормочных смесей
    path('',
         views_luremix.LureMixList.as_view(),
         name='lure_mix'),
    # Добавление прикормочной смеси
    path('add/',
         views_luremix.LureMixAdd.as_view(),
         name='lure_mix_add'),
    # Детали прикормочной смеси
    path('<int:lure_mix_id>/details/',
         views_luremix.LureMixDetails.as_view(),
         name='lure_mix_details'),
    # Редактирование прикормочной смеси
    path('<int:lure_mix_id>/edit/',
         views_luremix.LureMixEdit.as_view(),
         name='lure_mix_edit'),
    # Удаление прикормочной смеси
    path('<int:lure_mix_id>/delete/',
         views_luremix.LureMixDelete.as_view(),
         name='lure_mix_delete'),
    
    # Прикорм в прикормочной смеси
    # Выбор прикорма для смеси
    path('<int:lure_mix_id>/details/selectlure',
         views_luremix.SelectLureForMix.as_view(),
         name='select_lure_for_mix'),
    # Добавление прикорма в смесь
    path('<int:lure_mix_id>/details/addlure/<int:lure_base_id>',
         views_luremix.AddLureToMix.as_view(),
         name='add_lure_to_mix'),
    # Удалить прикорм из смеси
    path('<int:lure_mix_id>/details/reletelure/<int:lure_id>',
         views_luremix.DeleteLureOfMix.as_view(),
         name='delete_lure_of_mix'),
    # Редактирование прикорма в смесь
    path('<int:lure_mix_id>/details/editlure/<int:lure_id>',
         views_luremix.EditLureToMix.as_view(),
         name='edit_lure_to_mix'),
    
    # Аромы в прикормочной смеси
    # Выбор аромы для смеси
    path('<int:lure_mix_id>/details/selectaroma',
         views_luremix.SelectAromaForMix.as_view(),
         name='select_aroma_for_mix'),
    # Добавление аромы в прикорм
    path('<int:lure_mix_id>/details/addaroma/<int:aroma_base_id>',
         views_luremix.AddAromaToMix.as_view(),
         name='add_aroma_to_mix'),
    # Редактирование аромы в прикорме
    path('<int:lure_mix_id>/details/editaroma/<int:aroma_id>',
         views_luremix.EditAromaToMix.as_view(),
         name='edit_aroma_to_mix'),
    # Удаление аромы из прикорма
    path('<int:lure_mix_id>/deletearoma/<int:aroma_id>',
         views_luremix.DeleteAromaOfMix.as_view(),
         name='delete_aroma_of_mix'),

    # Добавки в прикорм
    # Выбор добавки в прикорм
    path('<int:lure_mix_id>/details/selectnozzle',
         views_luremix.SelectNozzleForMix.as_view(),
         name='select_nozzle_for_mix'),
    # Добавление добавки в прикорм
    path('<int:lure_mix_id>/details/addnozzle/<int:nozzle_base_id>',
         views_luremix.AddNozzleToMix.as_view(),
         name='add_nozzle_to_mix'),
    # Редактирование насадки или наживки в прикорме
    path('<int:lure_mix_id>/details/editnozzle/<int:nozzle_id>',
         views_luremix.EditNozzleToMix.as_view(),
         name='edit_nozzle_to_mix'),
    # Удаление насадки или наживки из прикорма
    path('<int:lure_mix_id>/deletenozzle/<int:nozzle_id>',
         views_luremix.DeleteNozzleOfMix.as_view(),
         name='delete_nozzle_of_mix'),
    ]
