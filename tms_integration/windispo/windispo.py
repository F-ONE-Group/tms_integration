import logging
import os
import shutil
import tempfile
from typing import Tuple, Union
from pydantic.dataclasses import dataclass

from tms_integration.utils.sftp import SftpBase

from .models import WindispoCreateJob, WindispoExportCreateJob

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s"
)


@dataclass
class Windispo(SftpBase):
    import_dest_folder: str
    output_target_folder: str = ""

    def import_auftrag(self, payload: WindispoCreateJob, import_prefix: str | None = None):
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            prefix=import_prefix,
            suffix=".xml",
            delete=False,
        ) as tmp_file:
            tmp_file.write(payload.generate_xml())
            tmp_file.close()
            self.import_file(tmp_file.name, self.import_dest_folder)

    @staticmethod
    def _normalize_identifier(value: str) -> str:
        return os.path.basename(value).strip().lower()

    def export_auftrag(
        self, identifier: str
    ) -> Union[Tuple[None, None], Tuple[str, WindispoExportCreateJob]]:
        if not self.output_target_folder:
            return None, None

        normalized_identifier = self._normalize_identifier(identifier)
        output_files = self.get_all_files(self.output_target_folder)
        dest_path = os.path.join(os.getcwd(), "tmp", "output")
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        os.makedirs(dest_path)

        for remote_file in output_files:
            filename = os.path.basename(remote_file)
            local_path = os.path.join(dest_path, filename)
            try:
                self.export_file(remote_file, local_path)
                with open(local_path, "r", encoding="utf-8") as xml_file:
                    payload = WindispoExportCreateJob.from_xml(xml_file.read())

                if (
                    self._normalize_identifier(payload.header.processed_file)
                    == normalized_identifier
                ):
                    return remote_file, payload
            except Exception:
                logging.exception(f"File [{remote_file}] cannot be accessed")

        return None, None
