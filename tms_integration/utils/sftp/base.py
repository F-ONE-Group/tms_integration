from typing import Optional
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
import pysftp


@dataclass
class SftpBase:

    class Credentials(BaseModel):
        host: str
        port: int = 22
        username: Optional[str]
        password: Optional[str]
        private_key: Optional[str]
        private_key_pass: Optional[str]

    credentials: Credentials

    def __post_init__(self):
        conn = pysftp.Connection(
            host=self.credentials.host,
            port=self.credentials.port,
            username=self.credentials.username,
            password=self.credentials.password,
            private_key=self.credentials.private_key,
            private_key_pass=self.credentials.private_key_pass,
        )
        conn.close()

    def import_file(self, source_filepath: str, dest_path: str) -> None:
        """
        Uploads a file from the source path to the destination path on the SFTP server.

        Args:
            credentials: The credentials required to establish an SFTP connection.
            source_filepath: The local path of the file to be uploaded.
            dest_path: The destination path on the SFTP server where the file will be uploaded.
        """
        with pysftp.Connection(
            host=self.credentials.host,
            port=self.credentials.port,
            username=self.credentials.username,
            password=self.credentials.password,
            private_key=self.credentials.private_key,
            private_key_pass=self.credentials.private_key_pass,
        ) as sftp:
            with sftp.cd(dest_path):
                sftp.put(source_filepath)

    def export_file(self, remote_filepath: str, local_filepath: str) -> None:
        """
        Export a file from a remote SFTP server using the provided credentials.

        Args:
            credentials (Credentials): The credentials needed to connect to the SFTP server.
            remote_filepath (str): The file path on the remote SFTP server.
            local_filepath (str): The local file path where the downloaded file will be saved.
        """
        with pysftp.Connection(
            host=self.credentials.host,
            port=self.credentials.port,
            username=self.credentials.username,
            password=self.credentials.password,
            private_key=self.credentials.private_key,
            private_key_pass=self.credentials.private_key_pass,
        ) as sftp:
            sftp.get(remote_filepath, local_filepath)
