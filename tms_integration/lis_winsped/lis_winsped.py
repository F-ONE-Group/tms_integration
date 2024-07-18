import tempfile
from .models import LisIn
from utils.sftp import SftpBase


class LisWinSped(SftpBase):
    import_dest_folder: str

    def import_auftrag(self, payload: LisIn, import_prefix: str = None):
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            prefix=import_prefix,
            suffix=".txt",
            delete=False,
        ) as tmp_file:
            tmp_file.write(payload.generate_txt())
            tmp_file.close()
            self.import_file(tmp_file.name, self.import_dest_folder)

    def export_auftrag(self):
        raise NotImplementedError
