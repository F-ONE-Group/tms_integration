import unittest
import xml.etree.ElementTree as ET

from tms_integration.windispo.models import (
    WindispoCreateJob,
    WindispoExportCreateJob,
    WindispoFile,
    WindispoHeader,
    WindispoJob,
    WindispoJobDetail,
)


class TestWindispoImportXml(unittest.TestCase):
    def test_generate_valid_createjob_v1_xml(self):
        payload = WindispoCreateJob(
            header=WindispoHeader(
                KdNr="39",
                MsgTime="20241127151739",
                MsgFrom="HB",
                ProcessType="new",
            ),
            job=WindispoJob(
                JobOwner="rs@windispo.at",
                ExtID="aaa1",
                AfKdNr="3",
                AfName1="Neele-Vat Transport B.V.",
                AfStraße="Bierbrouwerstraat 2",
                AfLand="NL",
                AfPlz="3194",
                AfOrt="Ap Hoogvliet",
                FzKdNr="3",
                FzName1="Neele-Vat Transport B.V.",
                FzStraße="Bierbrouwerstraat 2",
                FzLand="NL",
                FzPlz="3194",
                FzOrt="Ap Hoogvliet",
                Referenz="1802176771 FTL 90",
                FzgArt1="Planensattel",
                Whrg="EUR",
                jobdetail=[
                    WindispoJobDetail(
                        ZNr=1,
                        Laden=1,
                        Name1="Neele-Vat Transport BV",
                        Straße="Seattleweg 3",
                        Land="NL",
                        Plz="3195",
                        Ort="Pernis",
                        TerminVon="202208171100",
                        TerminBis="202208171430",
                        FixTermin=0,
                        Ladungsanzahl="66.00",
                        Ladungsart="Euro-Pal.",
                        Ladungsbezeichnung="Foodstuff",
                        Gewicht="4854.00",
                        ldm="13.60",
                        cbm="0.00",
                        Referenz="400154657",
                    ),
                    WindispoJobDetail(
                        ZNr=2,
                        Laden=2,
                        Name1="LSI Germany GmbH C/O Dachser",
                        Straße="Thomas Dachserstraße 4",
                        Land="DE",
                        Plz="90475",
                        Ort="Nürnberg",
                        TerminVon="202208180800",
                        TerminBis="202208181200",
                        FixTermin=0,
                        Ladungsanzahl="66.00",
                        Ladungsart="Euro-Pal.",
                        Ladungsbezeichnung="Foodstuff",
                        Gewicht="4854.00",
                        ldm="13.60",
                        cbm="0.00",
                        Referenz="PEU09722",
                    ),
                ],
                file=[
                    WindispoFile(
                        idx=1,
                        DocumentExtension=".msg",
                        AblageDatum="202208160922",
                        Betreff="Transport opdracht",
                        content="BASE64_CONTENT",
                    )
                ],
            ),
            jobcount=1,
        )

        xml_output = payload.generate_xml()
        root = ET.fromstring(xml_output)

        self.assertEqual(root.tag, "createjob.v1")
        self.assertEqual(root.findtext("jobcount"), "1")

        header = root.find("header")
        self.assertIsNotNone(header)
        assert header is not None  # for type checker
        self.assertEqual(header.findtext("KdNr"), "39")
        self.assertEqual(header.findtext("ProcessType"), "new")

        job = root.find("job")
        self.assertIsNotNone(job)
        assert job is not None  # for type checker
        self.assertEqual(job.findtext("AfStraße"), "Bierbrouwerstraat 2")
        self.assertEqual(job.findtext("FzStraße"), "Bierbrouwerstraat 2")

        jobdetails = job.findall("jobdetail")
        self.assertEqual(len(jobdetails), 2)
        self.assertEqual(job.findtext("jobdetailcount"), "2")

        files = job.findall("file")
        self.assertEqual(len(files), 1)
        self.assertEqual(job.findtext("filecount"), "1")
        self.assertEqual(files[0].attrib.get("idx"), "1")
        self.assertEqual(files[0].attrib.get("DocumentExtension"), ".msg")
        self.assertEqual(files[0].text, "BASE64_CONTENT")


class TestWindispoExportXml(unittest.TestCase):
    def test_parse_success_response(self):
        xml_response = (
            '<?xml version="1.0" encoding="utf-8"?>'
            "<createjob.v1>"
            "<header>"
            "<KdNr>71</KdNr>"
            "<MsgTime>20250219152455</MsgTime>"
            "<MsgFrom>TRAW</MsgFrom>"
            "<ProcessType>new accepted</ProcessType>"
            "<ProcessedFile>647496.xml</ProcessedFile>"
            "</header>"
            "<job>"
            "<DocID>2668/00</DocID>"
            "<ExtID>aaa1</ExtID>"
            "<AfKdNr>1487</AfKdNr>"
            "</job>"
            "<jobcount>1</jobcount>"
            "</createjob.v1>"
        )

        payload = WindispoExportCreateJob.from_xml(xml_response)

        self.assertEqual(payload.header.kd_nr, "71")
        self.assertEqual(payload.header.processed_file, "647496.xml")
        self.assertEqual(payload.job.doc_id, "2668/00")
        self.assertEqual(payload.job.ext_id, "aaa1")
        self.assertEqual(payload.job.af_kd_nr, "1487")
        self.assertIsNone(payload.job.error)

    def test_parse_failure_response(self):
        xml_response = (
            '<?xml version="1.0" encoding="utf-8"?>'
            "<createjob.v1>"
            "<header>"
            "<KdNr>71</KdNr>"
            "<MsgTime>20250219153331</MsgTime>"
            "<MsgFrom>TRAW</MsgFrom>"
            "<ProcessType>new failed</ProcessType>"
            "<ProcessedFile>647497.xml</ProcessedFile>"
            "</header>"
            "<job>"
            "<ExtID>aaa2</ExtID>"
            "<AfKdNr>3</AfKdNr>"
            "<Error><ErrorMsg>ExtID already used</ErrorMsg></Error>"
            "</job>"
            "<jobcount>1</jobcount>"
            "</createjob.v1>"
        )

        payload = WindispoExportCreateJob.from_xml(xml_response)

        self.assertEqual(payload.header.process_type, "new failed")
        self.assertIsNone(payload.job.doc_id)
        self.assertEqual(payload.job.ext_id, "aaa2")
        self.assertEqual(payload.job.af_kd_nr, "3")
        self.assertIsNotNone(payload.job.error)
        self.assertEqual(payload.job.error.error_msg, "ExtID already used")


if __name__ == "__main__":
    unittest.main()
