
(globalenv) D:\PROGRAMMING\projects-skripsi\prediksi_prestasi_akademik_siswa\sipas>python manage.py show_urls
/       core.views.index        core:dashboard
/academics/     academics.views.index   academics:index
/academics/akademik/    academics.akademik.web.views.index      academics:akademik:akademik_web:index
/academics/akademik/<int:id>/   academics.akademik.web.views.detail     academics:akademik:akademik_web:detail
/academics/akademik/<int:siswa_id>/create/      academics.akademik.web.views.create     academics:akademik:akademik_web:create
/academics/api/ rest_framework.routers.APIRootView      academics:academics_api:api-root
/academics/api/<drf_format_suffix:format>       rest_framework.routers.APIRootView      academics:academics_api:api-root
/academics/api/data-akademik/   academics.api.viewsets.DataAkademikViewSet      academics:academics_api:data-akademik-list
/academics/api/data-akademik/<pk>/      academics.api.viewsets.DataAkademikViewSet      academics:academics_api:data-akademik-detail
/academics/api/data-akademik/<pk>\.<format>/    academics.api.viewsets.DataAkademikViewSet      academics:academics_api:data-akademik-detail
/academics/api/data-akademik\.<format>/ academics.api.viewsets.DataAkademikViewSet      academics:academics_api:data-akademik-list
/academics/api/kehadiran/       academics.api.viewsets.KehadiranViewSet academics:academics_api:kehadiran-list
/academics/api/kehadiran/<pk>/  academics.api.viewsets.KehadiranViewSet academics:academics_api:kehadiran-detail
/academics/api/kehadiran/<pk>\.<format>/        academics.api.viewsets.KehadiranViewSet academics:academics_api:kehadiran-detail
/academics/api/kehadiran\.<format>/     academics.api.viewsets.KehadiranViewSet academics:academics_api:kehadiran-list
/academics/api/prediksi-prestasi/       academics.api.viewsets.PrediksiPrestasiViewSet  academics:academics_api:prediksi-prestasi-list
/academics/api/prediksi-prestasi/<pk>/  academics.api.viewsets.PrediksiPrestasiViewSet  academics:academics_api:prediksi-prestasi-detail
/academics/api/prediksi-prestasi/<pk>\.<format>/        academics.api.viewsets.PrediksiPrestasiViewSet  academics:academics_api:prediksi-prestasi-detail
/academics/api/prediksi-prestasi\.<format>/     academics.api.viewsets.PrediksiPrestasiViewSet  academics:academics_api:prediksi-prestasi-list
/academics/api/siswa/   academics.api.viewsets.SiswaViewSet     academics:academics_api:siswa-list
/academics/api/siswa/<pk>/      academics.api.viewsets.SiswaViewSet     academics:academics_api:siswa-detail
/academics/api/siswa/<pk>\.<format>/    academics.api.viewsets.SiswaViewSet     academics:academics_api:siswa-detail
/academics/api/siswa\.<format>/ academics.api.viewsets.SiswaViewSet     academics:academics_api:siswa-list
/academics/kehadiran/   academics.kehadiran.web.views.index     academics:kehadiran:kehadiran_web:index
/academics/kehadiran/<int:kehadiran_id>/        academics.kehadiran.web.views.detail    academics:kehadiran:kehadiran_web:detail
/academics/kehadiran/<int:siswa_id>/create/     academics.kehadiran.web.views.create    academics:kehadiran:kehadiran_web:create
/academics/siswa/       academics.siswa.web.views.index academics:siswa:siswa_web:index
/academics/siswa/<int:siswa_id>/        academics.siswa.web.views.siswa_detail_view     academics:siswa:siswa_web:detail
/academics/siswa/<int:siswa_id>/delete/ academics.siswa.web.views.siswa_delete_view     academics:siswa:siswa_web:delete
/academics/siswa/api/   rest_framework.routers.APIRootView      academics:siswa:siswa_api:api-root
/academics/siswa/api/<drf_format_suffix:format> rest_framework.routers.APIRootView      academics:siswa:siswa_api:api-root
/academics/siswa/api/data-akademik/     academics.api.viewsets.DataAkademikViewSet      academics:siswa:siswa_api:data-akademik-list
/academics/siswa/api/data-akademik/<pk>/        academics.api.viewsets.DataAkademikViewSet      academics:siswa:siswa_api:data-akademik-detail
/academics/siswa/api/data-akademik/<pk>\.<format>/      academics.api.viewsets.DataAkademikViewSet      academics:siswa:siswa_api:data-akademik-detail
/academics/siswa/api/data-akademik\.<format>/   academics.api.viewsets.DataAkademikViewSet      academics:siswa:siswa_api:data-akademik-list
/academics/siswa/api/kehadiran/ academics.api.viewsets.KehadiranViewSet academics:siswa:siswa_api:kehadiran-list
/academics/siswa/api/kehadiran/<pk>/    academics.api.viewsets.KehadiranViewSet academics:siswa:siswa_api:kehadiran-detail
/academics/siswa/api/kehadiran/<pk>\.<format>/  academics.api.viewsets.KehadiranViewSet academics:siswa:siswa_api:kehadiran-detail
/academics/siswa/api/kehadiran\.<format>/       academics.api.viewsets.KehadiranViewSet academics:siswa:siswa_api:kehadiran-list
/academics/siswa/api/prediksi-prestasi/ academics.api.viewsets.PrediksiPrestasiViewSet  academics:siswa:siswa_api:prediksi-prestasi-list
/academics/siswa/api/prediksi-prestasi/<pk>/    academics.api.viewsets.PrediksiPrestasiViewSet  academics:siswa:siswa_api:prediksi-prestasi-detail
/academics/siswa/api/prediksi-prestasi/<pk>\.<format>/  academics.api.viewsets.PrediksiPrestasiViewSet  academics:siswa:siswa_api:prediksi-prestasi-detail
/academics/siswa/api/prediksi-prestasi\.<format>/       academics.api.viewsets.PrediksiPrestasiViewSet  academics:siswa:siswa_api:prediksi-prestasi-list
/academics/siswa/api/siswa/     academics.api.viewsets.SiswaViewSet     academics:siswa:siswa_api:siswa-list
/academics/siswa/api/siswa/<pk>/        academics.api.viewsets.SiswaViewSet     academics:siswa:siswa_api:siswa-detail
/academics/siswa/api/siswa/<pk>\.<format>/      academics.api.viewsets.SiswaViewSet     academics:siswa:siswa_api:siswa-detail
/academics/siswa/api/siswa\.<format>/   academics.api.viewsets.SiswaViewSet     academics:siswa:siswa_api:siswa-list
/academics/siswa/list/  academics.siswa.web.views.siswa_list_view       academics:siswa:siswa_web:list
/accounts/      accounts.views.index    accounts:index
/accounts/api/guru/<int:guru_id>/       accounts.api.viewsets.GuruView  accounts:accounts_api:guru
/accounts/login/        accounts.views.login_view       accounts:login
/accounts/logout/       accounts.views.logout_view      accounts:logout
/accounts/profil/       accounts.views.profil   accounts:profil
/admin/ django.contrib.admin.sites.index        admin:index
/admin/<app_label>/     django.contrib.admin.sites.app_index    admin:app_list
/admin/<url>    django.contrib.admin.sites.catch_all_view
/admin/academics/dataakademik/  django.contrib.admin.options.changelist_view    admin:academics_dataakademik_changelist
/admin/academics/dataakademik/<path:object_id>/ django.views.generic.base.RedirectView
/admin/academics/dataakademik/<path:object_id>/change/  django.contrib.admin.options.change_view        admin:academics_dataakademik_change
/admin/academics/dataakademik/<path:object_id>/delete/  django.contrib.admin.options.delete_view        admin:academics_dataakademik_delete
/admin/academics/dataakademik/<path:object_id>/history/ django.contrib.admin.options.history_view       admin:academics_dataakademik_history
/admin/academics/dataakademik/add/      django.contrib.admin.options.add_view   admin:academics_dataakademik_add
/admin/academics/kehadiran/     django.contrib.admin.options.changelist_view    admin:academics_kehadiran_changelist
/admin/academics/kehadiran/<path:object_id>/    django.views.generic.base.RedirectView
/admin/academics/kehadiran/<path:object_id>/change/     django.contrib.admin.options.change_view        admin:academics_kehadiran_change
/admin/academics/kehadiran/<path:object_id>/delete/     django.contrib.admin.options.delete_view        admin:academics_kehadiran_delete
/admin/academics/kehadiran/<path:object_id>/history/    django.contrib.admin.options.history_view       admin:academics_kehadiran_history
/admin/academics/kehadiran/add/ django.contrib.admin.options.add_view   admin:academics_kehadiran_add
/admin/academics/prediksiprestasi/      django.contrib.admin.options.changelist_view    admin:academics_prediksiprestasi_changelist
/admin/academics/prediksiprestasi/<path:object_id>/     django.views.generic.base.RedirectView
/admin/academics/prediksiprestasi/<path:object_id>/change/      django.contrib.admin.options.change_view        admin:academics_prediksiprestasi_change
/admin/academics/prediksiprestasi/<path:object_id>/delete/      django.contrib.admin.options.delete_view        admin:academics_prediksiprestasi_delete
/admin/academics/prediksiprestasi/<path:object_id>/history/     django.contrib.admin.options.history_view       admin:academics_prediksiprestasi_history
/admin/academics/prediksiprestasi/add/  django.contrib.admin.options.add_view   admin:academics_prediksiprestasi_add
/admin/academics/siswa/ django.contrib.admin.options.changelist_view    admin:academics_siswa_changelist
/admin/academics/siswa/<path:object_id>/        django.views.generic.base.RedirectView
/admin/academics/siswa/<path:object_id>/change/ django.contrib.admin.options.change_view        admin:academics_siswa_change
/admin/academics/siswa/<path:object_id>/delete/ django.contrib.admin.options.delete_view        admin:academics_siswa_delete
/admin/academics/siswa/<path:object_id>/history/        django.contrib.admin.options.history_view       admin:academics_siswa_history
/admin/academics/siswa/add/     django.contrib.admin.options.add_view   admin:academics_siswa_add
/admin/accounts/admin/  django.contrib.admin.options.changelist_view    admin:accounts_admin_changelist
/admin/accounts/admin/<path:object_id>/ django.views.generic.base.RedirectView
/admin/accounts/admin/<path:object_id>/change/  django.contrib.admin.options.change_view        admin:accounts_admin_change
/admin/accounts/admin/<path:object_id>/delete/  django.contrib.admin.options.delete_view        admin:accounts_admin_delete
/admin/accounts/admin/<path:object_id>/history/ django.contrib.admin.options.history_view       admin:accounts_admin_history
/admin/accounts/admin/add/      django.contrib.admin.options.add_view   admin:accounts_admin_add
/admin/accounts/guru/   django.contrib.admin.options.changelist_view    admin:accounts_guru_changelist
/admin/accounts/guru/<path:object_id>/  django.views.generic.base.RedirectView
/admin/accounts/guru/<path:object_id>/change/   django.contrib.admin.options.change_view        admin:accounts_guru_change
/admin/accounts/guru/<path:object_id>/delete/   django.contrib.admin.options.delete_view        admin:accounts_guru_delete
/admin/accounts/guru/<path:object_id>/history/  django.contrib.admin.options.history_view       admin:accounts_guru_history
/admin/accounts/guru/add/       django.contrib.admin.options.add_view   admin:accounts_guru_add
/admin/auth/group/      django.contrib.admin.options.changelist_view    admin:auth_group_changelist
/admin/auth/group/<path:object_id>/     django.views.generic.base.RedirectView
/admin/auth/group/<path:object_id>/change/      django.contrib.admin.options.change_view        admin:auth_group_change
/admin/auth/group/<path:object_id>/delete/      django.contrib.admin.options.delete_view        admin:auth_group_delete
/admin/auth/group/<path:object_id>/history/     django.contrib.admin.options.history_view       admin:auth_group_history
/admin/auth/group/add/  django.contrib.admin.options.add_view   admin:auth_group_add
/admin/auth/user/       django.contrib.admin.options.changelist_view    admin:auth_user_changelist
/admin/auth/user/<id>/password/ django.contrib.auth.admin.user_change_password  admin:auth_user_password_change
/admin/auth/user/<path:object_id>/      django.views.generic.base.RedirectView
/admin/auth/user/<path:object_id>/change/       django.contrib.admin.options.change_view        admin:auth_user_change
/admin/auth/user/<path:object_id>/delete/       django.contrib.admin.options.delete_view        admin:auth_user_delete
/admin/auth/user/<path:object_id>/history/      django.contrib.admin.options.history_view       admin:auth_user_history
/admin/auth/user/add/   django.contrib.auth.admin.add_view      admin:auth_user_add
/admin/autocomplete/    django.contrib.admin.sites.autocomplete_view    admin:autocomplete
/admin/jsi18n/  django.contrib.admin.sites.i18n_javascript      admin:jsi18n
/admin/login/   django.contrib.admin.sites.login        admin:login
/admin/logout/  django.contrib.admin.sites.logout       admin:logout
/admin/password_change/ django.contrib.admin.sites.password_change      admin:password_change
/admin/password_change/done/    django.contrib.admin.sites.password_change_done admin:password_change_done
/admin/predictions/dataset/     django.contrib.admin.options.changelist_view    admin:predictions_dataset_changelist
/admin/predictions/dataset/<path:object_id>/    django.views.generic.base.RedirectView
/admin/predictions/dataset/<path:object_id>/change/     django.contrib.admin.options.change_view        admin:predictions_dataset_change
/admin/predictions/dataset/<path:object_id>/delete/     django.contrib.admin.options.delete_view        admin:predictions_dataset_delete
/admin/predictions/dataset/<path:object_id>/history/    django.contrib.admin.options.history_view       admin:predictions_dataset_history
/admin/predictions/dataset/add/ django.contrib.admin.options.add_view   admin:predictions_dataset_add
/admin/predictions/datasetusage/        django.contrib.admin.options.changelist_view    admin:predictions_datasetusage_changelist
/admin/predictions/datasetusage/<path:object_id>/       django.views.generic.base.RedirectView
/admin/predictions/datasetusage/<path:object_id>/change/        django.contrib.admin.options.change_view        admin:predictions_datasetusage_change
/admin/predictions/datasetusage/<path:object_id>/delete/        django.contrib.admin.options.delete_view        admin:predictions_datasetusage_delete
/admin/predictions/datasetusage/<path:object_id>/history/       django.contrib.admin.options.history_view       admin:predictions_datasetusage_history
/admin/predictions/datasetusage/add/    django.contrib.admin.options.add_view   admin:predictions_datasetusage_add
/admin/predictions/datasetversion/      django.contrib.admin.options.changelist_view    admin:predictions_datasetversion_changelist
/admin/predictions/datasetversion/<path:object_id>/     django.views.generic.base.RedirectView
/admin/predictions/datasetversion/<path:object_id>/change/      django.contrib.admin.options.change_view        admin:predictions_datasetversion_change
/admin/predictions/datasetversion/<path:object_id>/delete/      django.contrib.admin.options.delete_view        admin:predictions_datasetversion_delete
/admin/predictions/datasetversion/<path:object_id>/history/     django.contrib.admin.options.history_view       admin:predictions_datasetversion_history
/admin/predictions/datasetversion/add/  django.contrib.admin.options.add_view   admin:predictions_datasetversion_add
/admin/predictions/hasilprediksi/       django.contrib.admin.options.changelist_view    admin:predictions_hasilprediksi_changelist
/admin/predictions/hasilprediksi/<path:object_id>/      django.views.generic.base.RedirectView
/admin/predictions/hasilprediksi/<path:object_id>/change/       django.contrib.admin.options.change_view        admin:predictions_hasilprediksi_change
/admin/predictions/hasilprediksi/<path:object_id>/delete/       django.contrib.admin.options.delete_view        admin:predictions_hasilprediksi_delete
/admin/predictions/hasilprediksi/<path:object_id>/history/      django.contrib.admin.options.history_view       admin:predictions_hasilprediksi_history
/admin/predictions/hasilprediksi/add/   django.contrib.admin.options.add_view   admin:predictions_hasilprediksi_add
/admin/predictions/hasiltraining/       django.contrib.admin.options.changelist_view    admin:predictions_hasiltraining_changelist
/admin/predictions/hasiltraining/<path:object_id>/      django.views.generic.base.RedirectView
/admin/predictions/hasiltraining/<path:object_id>/change/       django.contrib.admin.options.change_view        admin:predictions_hasiltraining_change
/admin/predictions/hasiltraining/<path:object_id>/delete/       django.contrib.admin.options.delete_view        admin:predictions_hasiltraining_delete
/admin/predictions/hasiltraining/<path:object_id>/history/      django.contrib.admin.options.history_view       admin:predictions_hasiltraining_history
/admin/predictions/hasiltraining/add/   django.contrib.admin.options.add_view   admin:predictions_hasiltraining_add
/admin/predictions/modelml/     django.contrib.admin.options.changelist_view    admin:predictions_modelml_changelist
/admin/predictions/modelml/<path:object_id>/    django.views.generic.base.RedirectView
/admin/predictions/modelml/<path:object_id>/change/     django.contrib.admin.options.change_view        admin:predictions_modelml_change
/admin/predictions/modelml/<path:object_id>/delete/     django.contrib.admin.options.delete_view        admin:predictions_modelml_delete
/admin/predictions/modelml/<path:object_id>/history/    django.contrib.admin.options.history_view       admin:predictions_modelml_history
/admin/predictions/modelml/add/ django.contrib.admin.options.add_view   admin:predictions_modelml_add
/admin/predictions/trainingrun/ django.contrib.admin.options.changelist_view    admin:predictions_trainingrun_changelist
/admin/predictions/trainingrun/<path:object_id>/        django.views.generic.base.RedirectView
/admin/predictions/trainingrun/<path:object_id>/change/ django.contrib.admin.options.change_view        admin:predictions_trainingrun_change
/admin/predictions/trainingrun/<path:object_id>/delete/ django.contrib.admin.options.delete_view        admin:predictions_trainingrun_delete
/admin/predictions/trainingrun/<path:object_id>/history/        django.contrib.admin.options.history_view       admin:predictions_trainingrun_history
/admin/predictions/trainingrun/add/     django.contrib.admin.options.add_view   admin:predictions_trainingrun_add
/admin/r/<path:content_type_id>/<path:object_id>/       django.contrib.contenttypes.views.shortcut      admin:view_on_site
/media/<path>   django.views.static.serve
/predictions/   predictions.web.views.PredictionView    predictions:predictions_web:index
/predictions/api/latih-model/   predictions.api.viewsets.LatihModelView predictions:predictions_api:latih_model
/predictions/api/submit-prediksi/       predictions.api.viewsets.AdminPredictionView    predictions:predictions_api:submit_prediksi
/predictions/datasets/<path>    django.views.static.serve
/predictions/ml_models/<path>   django.views.static.serve
/predictions/settings/  predictions.web.views.SettingsView      predictions:predictions_web:settings

(globalenv) D:\PROGRAMMING\projects-skripsi\prediksi_prestasi_akademik_siswa\sipas>