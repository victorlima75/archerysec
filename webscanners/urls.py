#                   _
#    /\            | |
#   /  \   _ __ ___| |__   ___ _ __ _   _
#  / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
# / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                    __/ |
#                                   |___/
# Copyright (C) 2017-2018 ArcherySec
# This file is part of ArcherySec Project.

from django.conf.urls import url
from webscanners import web_views

app_name = 'webscanners'

urlpatterns = [
    url(r'^login/$',
        web_views.login,
        name='login'),
    url(r'^signup/$',
        web_views.signup,
        name='signup'),
    url(r'^auth/$',
        web_views.auth_view,
        name='auth'),
    url(r'^logout/$',
        web_views.logout,
        name='logout'),
    url(r'^loggedin/$',
        web_views.loggedin,
        name='loggedin'),
    url(r'^$',
        web_views.index,
        name='index'),
    url(r'^scan_launch$',
        web_views.web_scan,
        name='web_scan'),
    url(r'^vuln_list/',
        web_views.scan_list,
        name='vuln_list'),
    url(r'^web_vuln_list/',
        web_views.list_web_vuln,
        name='web_vuln'),
    url(r'^vuln_details/',
        web_views.vuln_details,
        name='vuln_details'),
    url(r'^setting/',
        web_views.setting,
        name='setting'),
    url(r'^zapsetting/',
        web_views.zap_setting,
        name='zap_setting'),
    url(r'^setting_edit/',
        web_views.zap_set_update,
        name='setting_edit'),
    url(r'^scans_list',
        web_views.scan_list,
        name='setting'),
    url(r'^scans_table',
        web_views.scan_table,
        name='scans_table'),
    url(r'^del_scan',
        web_views.del_scan,
        name='del_scan'),
    url(r'^zap_vul_details',
        web_views.vuln_details,
        name='zap_vul_details'),
    url(r'^dashboard',
        web_views.dashboard,
        name='dashboard'),
    url(r'^net_dashboard',
        web_views.dashboard_network,
        name='net_dashboard'),
    url(r'^sel_login',
        web_views.sel_login,
        name='sel'),
    url(r'save_cookie',
        web_views.save_cookie,
        name='save_cookie'),
    url(r'exclude_url',
        web_views.exclude_url,
        name='exclude_url'),
    url(r'^edit_vuln',
        web_views.edit_vuln,
        name='edit_vuln'),
    url(r'^del_vuln',
        web_views.del_vuln,
        name='del_vuln'),
    url(r'^vuln_dat',
        web_views.vuln_check,
        name='vuln_dat'),
    url(r'^edit_vuln_dat',
        web_views.edit_vuln_check,
        name='edit_vuln_dat'),
    url(r'^add_vuln',
        web_views.add_vuln,
        name='add_vuln'),
    url(r'^create_vuln',
        web_views.create_vuln,
        name='create_vuln'),
    url(r'^get_scan_pdf',
        web_views.scan_pdf_gen),
    url(r'^zap_rescan',
        web_views.zap_rescan),
    url(r'^cookies_list',
        web_views.cookies_list),
    url(r'^cookies_del',
        web_views.del_cookies),
    url(r'^excluded_url_list',
        web_views.exluded_url_list),

    # Burp Setting from path
    url(r'^burp_setting',
        web_views.burp_setting,
        name='burp_setting'),
    # Burp scans
    url(r'^burp_launch_scan',
        web_views.burp_scan_launch,
        name='burp_scan_launch'),
    url(r'^burp_scan_list',
        web_views.burp_scan_list,
        name='burp_scan_list'),
    url(r'^burp_vuln_list',
        web_views.burp_list_vuln,
        name='burp_vuln_list'),
    url(r'^burp_vuln_data',
        web_views.burp_vuln_data,
        name='burp_vuln_data'),
    url(r'^burp_vuln_out',
        web_views.burp_vuln_out,
        name='burp_vuln_out'),
    url(r'^del_burp_scan',
        web_views.del_burp_scan,
        name='del_burp_scan'),
    url(r'^del_burp_vuln',
        web_views.del_burp_vuln,
        name='del_burp_vuln'),
    url(r'^edit_burp_vuln',
        web_views.edit_burp_vuln,
        name='edit_burp_vuln'),
    url(r'^xml_upload',
        web_views.xml_upload,
        name='xml_upload'),
    url(r'^email_setting',
        web_views.email_setting,
        name='email_setting', ),
    url(r'^cookie_add',
        web_views.add_cookies,
        name='add_cookies', ),

    # arachni
    url(r'^arachni_list_vuln',
        web_views.arachni_list_vuln,
        name='arachni_list_vuln'),
    url(r'^arachni_scan_list',
        web_views.arachni_scan_list,
        name='arachni_scan_list'),
    url(r'^arachni_vuln_data',
        web_views.arachni_vuln_data,
        name='arachni_vuln_data'),
    url(r'^arachni_vuln_out',
        web_views.arachni_vuln_out,
        name='arachni_vuln_out'),
    url(r'^del_arachni_scan',
        web_views.del_arachni_scan,
        name='del_arachni_scan'),
    url(r'^arachni_del_vuln',
        web_views.arachni_del_vuln,
        name='arachni_del_vuln'),

    url(r'^web_task_launch',
        web_views.web_task_launch,
        name='web_task_launch'),

    url(r'^web_scan_schedule',
        web_views.web_scan_schedule,
        name='web_scan_schedule'),

    url(r'^del_web_scan_schedule',
        web_views.del_web_scan_schedule,
        name='del_web_scan_schedule'),

    # All netsparker URL's
    url(r'^netsparker_list_vuln',
        web_views.netsparker_list_vuln,
        name='netsparker_list_vuln'),
    url(r'^netsparker_scan_list',
        web_views.netsparker_scan_list,
        name='netsparker_scan_list'),
    url(r'^netsparker_vuln_data',
        web_views.netsparker_vuln_data,
        name='netsparker_vuln_data'),
    url(r'^netsparker_vuln_out',
        web_views.netsparker_vuln_out,
        name='netsparker_vuln_out'),
    url(r'^del_netsparker_scan',
        web_views.del_netsparker_scan,
        name='del_netsparker_scan'),
    url(r'^netsparker_del_vuln',
        web_views.netsparker_del_vuln,
        name='netsparker_del_vuln'),

    # All webinspect URL's
    url(r'^webinspect_list_vuln',
        web_views.webinspect_list_vuln,
        name='webinspect_list_vuln'),
    url(r'^webinspect_scan_list',
        web_views.webinspect_scan_list,
        name='webinspect_scan_list'),
    url(r'^webinspect_vuln_data',
        web_views.webinspect_vuln_data,
        name='webinspect_vuln_data'),
    url(r'^webinspect_vuln_out',
        web_views.webinspect_vuln_out,
        name='webinspect_vuln_out'),
    url(r'^del_webinspect_scan',
        web_views.del_webinspect_scan,
        name='del_webinspect_scan'),
    url(r'^webinspect_del_vuln',
        web_views.webinspect_del_vuln,
        name='webinspect_del_vuln'),

]
