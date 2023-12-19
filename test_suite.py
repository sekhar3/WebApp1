# 1. Import the files
import unittest
from tests.test_holder.test_create_new_account import TestCreateAccount
from tests.test_holder.test_add_dependents import TestAddDependent
from tests.test_holder.test_schedule_appointment_virtual_appointment_inspire_health import \
    TestScheduleVirtualAppointment
from tests.test_holder.test_schedule_virtual_appointment_for_dependent import TestScheduleVirtualAppointmentDependent
from tests.test_holder.test_schedule_appointment_covid_testing_virtual_dependent import TestScheduleCovidTestingVirtualAppointmentDependent
from tests.test_holder.test_schedule_appointment_covid_testing_virtual import TestScheduleCovidTestingVirtualAppointment
from tests.test_holder.test_schedule_appointment_medical_test_antibody_cvs_pharmacy import TestScheduleAppointmentMACP
from tests.test_holder.test_schedule_appointment_medical_test_antibody_inspire_health import TestScheduleAppointmentMACI
from tests.test_holder.test_schedule_appointment_medical_test_antigen_cvs_pharmacy import TestScheduleAppointmentMAC
from tests.test_holder.test_schedule_appointment_medical_test_antigen_inspire_health import TestScheduleAppointmentMAIH
from tests.test_holder.test_schedule_appointment_medical_test_pcr_cvs_pharmacy import TestScheduleAppointmentMPCP
from tests.test_holder.test_schedule_appointment_medical_test_pcr_inspire_health import TestScheduleAppointmentMPIH
from tests.test_holder.test_schedule_appointment_vaccination_covid_19_vaccine_inspire_health import \
    TestScheduleAppointmentCVIH
from tests.test_holder.test_schedule_appointment_vaccination_covid_19_vaccine_cvs_pharmacy import \
    TestScheduleAppointmentCVCP
from tests.test_holder.test_schedule_appointment_for_dependent import TestScheduleAppointmentDependent
from tests.test_holder.test_home_kit_order_antibody import TestHomeOrderKitAntibody
from tests.test_holder.test_home_kit_order_antigen import TestHomeOrderKitAntigen
from tests.test_holder.test_home_kit_order_antigen_self_kit import TestHomeOrderKitSelfKit
from tests.test_holder.test_home_kit_order_antigen1 import TestHomeOrderKitAntigen1
from tests.test_holder.test_home_kit_order_non_zero_product import TestHomeOrderNonZeroProduct
from tests.test_holder.test_home_kit_order_pcr import TestHomeOrderKitPcr
from tests.test_holder.test_cancel_scheduled_appointment import TestCancelScheduleAppointment
from tests.test_holder.test_cancel_schedule_appointment_dependent import TestCancelDependentScheduleAppointment
from tests.test_holder.test_enable_email_notifications import TestNotificationPreferencesEnableEmail
from tests.test_holder.test_enable_push_notifications import TestNotificationPreferencesEnablePush
from tests.test_holder.test_enable_sms_notifications import TestNotificationPreferencesEnableSMS
from tests.test_holder.test_disable_email_notifications import TestNotificationPreferencesDisableEmail
from tests.test_holder.test_disable_push_notifications import TestNotificationPreferencesDisablePush
from tests.test_holder.test_disable_sms_notifications import TestNotificationPreferencesDisableSMS
from tests.test_holder.test_download_qr_code import TestDownloadQRCode
from tests.test_holder.test_reset_id import TestResetUPassId
from tests.test_holder.test_view_scan_history import TestViewScanHistory
from tests.test_holder.test_link_record_health_Covid_PCR_Test import TestLinkRecordHealthCovidPcr
from tests.test_holder.test_link_record_health_Covid_PCR_Test_for_dependent import TestLinkRecordHealthCovidPcrDependent
from tests.test_holder.test_link_record_health_Covid_vaccination_CDC import TestLinkRecordHealthCovidVaccinationCDC
from tests.test_holder.test_link_record_health_Covid_vaccination_CDC_dependent import \
    TestLinkRecordHealthCovidVaccinationCDCDependent
from tests.test_holder.test_link_record_health_Covid_vaccination_inspire_health_dependent import \
    TestLinkRecordHealthCovidVaccinationInspireHealthDependent
from tests.test_holder.test_link_record_health_Covid_vaccination_inspire_health import \
    TestLinkRecordHealthCovidVaccinationInspireHealth
from tests.test_holder.test_link_record_health_Covid_19_rt_pcr import TestLinkRecordHealthCovid19RTPCR
from tests.test_holder.test_link_record_health_Covid_19_rt_pcr_dependent import \
    TestLinkRecordHealthCovid19RTPCRDependent
from tests.test_holder.test_link_record_health_Covid_19_Test_Antibody import TestLinkRecordHealthCovid19Antibody
from tests.test_holder.test_link_record_health_Covid_19_Test_Antibody_dependent import \
    TestLinkRecordHealthCovid19AntibodyDependent
from tests.test_holder.test_link_record_health_COVID_19_Test_Antigen_CDC import TestLinkRecordHealthCovid19AntigenCdc
from tests.test_holder.test_link_record_health_COVID_19_Test_Antigen_CDC_dependent import \
    TestLinkRecordHealthCovid19AntigenCdcDependent
from tests.test_holder.test_link_record_health_COVID_19_Test_Antigen_inspire_health import \
    TestLinkRecordHealthCovid19Antigen
from tests.test_holder.test_link_record_health_COVID_19_Test_Antigen_inspire_health_dependent import \
    TestLinkRecordHealthCovid19AntigenInspireHealthDependent
from tests.test_holder.test_link_record_health_Immunization import TestLinkRecordHealthImmunization
from tests.test_holder.test_link_record_health_Immunization_dependent import TestLinkRecordHealthImmunizationD
from tests.test_holder.test_link_record_id_alabama_driver_license import TestLinkRecordIdAlabamaDriverLicense
from tests.test_holder.test_link_record_id_alabama_driver_license_dependent import \
    TestLinkRecordIdDriverLicenseDependent
from tests.test_holder.test_link_record_id_passport import TestLinkRecordIdPassport
from tests.test_holder.test_link_record_id_passport_dependent import TestLinkRecordIdPassportDependent
from tests.test_holder.test_link_record_id_student_card import TestLinkRecordIdStudentCard
from tests.test_holder.test_link_record_id_student_card_dependent import TestLinkRecordIdStudentCardDependent
from tests.test_holder.test_link_record_id_texas_driver_license import TestLinkRecordIdTexasDriverLicense
from tests.test_holder.test_link_record_id_texas_driver_license_dependent import \
    TestLinkRecordIdTexasDriverLicenseDependent
from tests.test_holder.test_edit_basic_information import TestEditBasicInfo
from tests.test_holder.test_edit_contact_information import TestEditContactInfo
from tests.test_holder.test_edit_additional_profile_information import TestEditAdditionalProfileInfo
from tests.test_holder.test_edit_dependent_account_details import TestDependentAccountDetails
from tests.test_holder.test_edit_dependent_additional_profile_info import TestDependentProfileInformation
from tests.test_holder.test_delete_dependent import TestDeleteDependent
from tests.test_holder.test_delete_account import TestDeleteAccount

# 2. Create the object of the class using unitTest
create_account = unittest.TestLoader().loadTestsFromTestCase(TestCreateAccount)
add_dependent = unittest.TestLoader().loadTestsFromTestCase(TestAddDependent)
covid_virtual = unittest.TestLoader().loadTestsFromTestCase(TestScheduleCovidTestingVirtualAppointment)
covid_virtual_d = unittest.TestLoader().loadTestsFromTestCase(TestScheduleCovidTestingVirtualAppointmentDependent)
# virtual_appointment = unittest.TestLoader().loadTestsFromTestCase(TestScheduleVirtualAppointment)
# dependent_v_a = unittest.TestLoader().loadTestsFromTestCase(TestScheduleVirtualAppointmentDependent)
schedule_mcap = unittest.TestLoader().loadTestsFromTestCase(TestScheduleAppointmentMACP)
schedule_maci = unittest.TestLoader().loadTestsFromTestCase(TestScheduleAppointmentMACI)
schedule_mac = unittest.TestLoader().loadTestsFromTestCase(TestScheduleAppointmentMAC)
schedule_maih = unittest.TestLoader().loadTestsFromTestCase(TestScheduleAppointmentMAIH)
schedule_mpcp = unittest.TestLoader().loadTestsFromTestCase(TestScheduleAppointmentMPCP)
schedule_mpih = unittest.TestLoader().loadTestsFromTestCase(TestScheduleAppointmentMPIH)
schedule_cvih = unittest.TestLoader().loadTestsFromTestCase(TestScheduleAppointmentCVIH)
schedule_cvcp = unittest.TestLoader().loadTestsFromTestCase(TestScheduleAppointmentCVCP)
schedule_dependent = unittest.TestLoader().loadTestsFromTestCase(TestScheduleAppointmentDependent)
order_pcr = unittest.TestLoader().loadTestsFromTestCase(TestHomeOrderKitPcr)
order_antigen = unittest.TestLoader().loadTestsFromTestCase(TestHomeOrderKitAntigen1)
order_non_zero_product = unittest.TestLoader().loadTestsFromTestCase(TestHomeOrderNonZeroProduct)
cancel_appointment = unittest.TestLoader().loadTestsFromTestCase(TestCancelScheduleAppointment)
cancel_appointment_d = unittest.TestLoader().loadTestsFromTestCase(TestCancelDependentScheduleAppointment)
enable_email = unittest.TestLoader().loadTestsFromTestCase(TestNotificationPreferencesEnableEmail)
enable_push = unittest.TestLoader().loadTestsFromTestCase(TestNotificationPreferencesEnablePush)
enable_sms = unittest.TestLoader().loadTestsFromTestCase(TestNotificationPreferencesEnableSMS)
disable_email = unittest.TestLoader().loadTestsFromTestCase(TestNotificationPreferencesDisableEmail)
disable_push = unittest.TestLoader().loadTestsFromTestCase(TestNotificationPreferencesDisablePush)
disable_sms = unittest.TestLoader().loadTestsFromTestCase(TestNotificationPreferencesDisableSMS)
qr_code = unittest.TestLoader().loadTestsFromTestCase(TestDownloadQRCode)
reset_id = unittest.TestLoader().loadTestsFromTestCase(TestResetUPassId)
view_scan = unittest.TestLoader().loadTestsFromTestCase(TestViewScanHistory)
record_pcr = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovidPcr)
record_pcr_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovidPcrDependent)
record_vcdc = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovidVaccinationCDC)
record_vcdc_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovidVaccinationCDCDependent)
record_vih = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovidVaccinationInspireHealth)
record_vih_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovidVaccinationInspireHealthDependent)
record_rtpcr = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovid19RTPCR)
record_rtpcr_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovid19RTPCRDependent)
record_antibody = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovid19Antibody)
record_antibody_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovid19AntibodyDependent)
record_antigen_cdc = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovid19AntigenCdc)
record_antigen_cdc_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovid19AntigenCdcDependent)
record_antigen = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovid19Antigen)
record_antigen_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthCovid19AntigenInspireHealthDependent)
record_immunization = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthImmunization)
record_immunization_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordHealthImmunizationD)
record_adl = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordIdAlabamaDriverLicense)
record_adl_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordIdDriverLicenseDependent)
record_passport = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordIdPassport)
record_passport_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordIdPassportDependent)
record_student_card = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordIdStudentCard)
record_student_card_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordIdStudentCardDependent)
record_tdl = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordIdTexasDriverLicense)
record_tdl_d = unittest.TestLoader().loadTestsFromTestCase(TestLinkRecordIdTexasDriverLicenseDependent)
edit_basic_info = unittest.TestLoader().loadTestsFromTestCase(TestEditBasicInfo)
edit_contact_info = unittest.TestLoader().loadTestsFromTestCase(TestEditContactInfo)
edit_add_info = unittest.TestLoader().loadTestsFromTestCase(TestEditAdditionalProfileInfo)
edit_d_info = unittest.TestLoader().loadTestsFromTestCase(TestDependentAccountDetails)
edit_d_add_info = unittest.TestLoader().loadTestsFromTestCase(TestDependentProfileInformation)
del_dependent = unittest.TestLoader().loadTestsFromTestCase(TestDeleteDependent)
del_account = unittest.TestLoader().loadTestsFromTestCase(TestDeleteAccount)

# 3. Create TestSuite
regressionTest = unittest.TestSuite([create_account, add_dependent,covid_virtual,covid_virtual_d,schedule_mcap,
                                     schedule_maci,schedule_mac,schedule_maih,schedule_mpcp,schedule_mpih,schedule_cvih,
                                     schedule_cvcp,schedule_dependent,order_pcr,order_antigen,order_non_zero_product,
                                     cancel_appointment,cancel_appointment_d,enable_email,enable_push,enable_sms,
                                     disable_email,disable_push,disable_sms,qr_code,reset_id,view_scan,record_pcr,
                                     record_pcr_d,record_vcdc,record_vcdc_d,record_vih,record_vih_d,record_rtpcr,
                                     record_rtpcr_d,record_antibody,record_antibody_d,record_antigen_cdc,
                                     record_antigen_cdc_d,record_antigen,record_antigen_d,record_immunization,
                                     record_immunization_d,record_adl,record_adl_d,record_passport,record_passport_d,
                                     record_student_card,record_student_card_d,record_tdl,record_tdl_d,edit_basic_info,
                                     edit_contact_info,edit_add_info,edit_d_info,edit_d_add_info,del_dependent,
                                     del_account])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

# Note : All the methods in test files should define in proper run order
