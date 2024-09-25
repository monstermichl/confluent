from __future__ import annotations
import os

from ..base.distributor_base import DistributorBase


class TargetPathDoesntExitException(Exception):
    def __init__(self, target_path: str):
        super().__init__(
            f'The target path {target_path} doesn\'t exist')


class FsDistributor(DistributorBase):
    def __init__(self, target_path: str, create_dirs: bool):
        """
        Constructor

        :param target_path: Relative target path within the repo.
        :type target_path:  str
        :param create_dirs: If true, the corresponding parent directories will be created on
                            distribute if they don't exist.
        :type create_dirs:  bool
        """
        super().__init__()

        self._target_path = target_path if target_path else ''  # Use current directory as default path.
        self._create_dirs = create_dirs

    def distribute(self, file_name: str, data: str) -> FsDistributor:
        """
        Method to distribute a generated config to a local filesystem location.

        :param file_name: Config file name.
        :type file_name:  str
        :param data:      Config file data.
        :type data:       str

        :raises TargetPathDoesntExitException: Raised if the target path doesn't exist.

        :return: The current FsDistributor instance.
        :rtype:  FsDistributor
        """
        if not os.path.exists(self._target_path):
            if self._create_dirs:
                os.makedirs(self._target_path, exist_ok=True)
            else:
                raise TargetPathDoesntExitException(self._target_path)

        # Write file to target-path.
        with open(os.path.join(self._target_path, file_name), 'w') as f:
            f.write(data)
        return self
