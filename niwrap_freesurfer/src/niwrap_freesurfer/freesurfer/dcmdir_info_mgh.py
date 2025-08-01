# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DCMDIR_INFO_MGH_METADATA = Metadata(
    id="8a0c29bc82d0c5ee9d5b9085f7f1bd5a728df60b.boutiques",
    name="dcmdir-info-mgh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


DcmdirInfoMghParameters = typing.TypedDict('DcmdirInfoMghParameters', {
    "__STYXTYPE__": typing.Literal["dcmdir-info-mgh"],
    "dicomdir": str,
    "unpackdir": typing.NotRequired[str | None],
    "version": bool,
    "help": bool,
    "nopre": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "dcmdir-info-mgh": dcmdir_info_mgh_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "dcmdir-info-mgh": dcmdir_info_mgh_outputs,
    }.get(t)


class DcmdirInfoMghOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcmdir_info_mgh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    converted_mgz_files: OutputPathType
    """Converted DICOM files to MGZ format with naming sequencename_runR.mgz,
    where R is the run number"""


def dcmdir_info_mgh_params(
    dicomdir: str,
    unpackdir: str | None = None,
    version: bool = False,
    help_: bool = False,
    nopre: bool = False,
) -> DcmdirInfoMghParameters:
    """
    Build parameters.
    
    Args:
        dicomdir: Input DICOM directory.
        unpackdir: Directory where the unpacked data will be stored (optional).\
            If specified, DICOM files are converted to MGZ format.
        version: Print version and exit.
        help_: Print help and exit.
        nopre: Do not assume filenames use the NNNNNN- prefix convention.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dcmdir-info-mgh",
        "dicomdir": dicomdir,
        "version": version,
        "help": help_,
        "nopre": nopre,
    }
    if unpackdir is not None:
        params["unpackdir"] = unpackdir
    return params


def dcmdir_info_mgh_cargs(
    params: DcmdirInfoMghParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("dcmdir-info-mgh")
    cargs.extend([
        "-mgh",
        params.get("dicomdir")
    ])
    if params.get("unpackdir") is not None:
        cargs.append(params.get("unpackdir"))
    if params.get("version"):
        cargs.append("--version")
    if params.get("help"):
        cargs.append("--help")
    if params.get("nopre"):
        cargs.append("--nopre")
    return cargs


def dcmdir_info_mgh_outputs(
    params: DcmdirInfoMghParameters,
    execution: Execution,
) -> DcmdirInfoMghOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DcmdirInfoMghOutputs(
        root=execution.output_file("."),
        converted_mgz_files=execution.output_file("sequencename_run*.mgz"),
    )
    return ret


def dcmdir_info_mgh_execute(
    params: DcmdirInfoMghParameters,
    execution: Execution,
) -> DcmdirInfoMghOutputs:
    """
    Scans a DICOM directory and extracts information about each series.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DcmdirInfoMghOutputs`).
    """
    params = execution.params(params)
    cargs = dcmdir_info_mgh_cargs(params, execution)
    ret = dcmdir_info_mgh_outputs(params, execution)
    execution.run(cargs)
    return ret


def dcmdir_info_mgh(
    dicomdir: str,
    unpackdir: str | None = None,
    version: bool = False,
    help_: bool = False,
    nopre: bool = False,
    runner: Runner | None = None,
) -> DcmdirInfoMghOutputs:
    """
    Scans a DICOM directory and extracts information about each series.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        dicomdir: Input DICOM directory.
        unpackdir: Directory where the unpacked data will be stored (optional).\
            If specified, DICOM files are converted to MGZ format.
        version: Print version and exit.
        help_: Print help and exit.
        nopre: Do not assume filenames use the NNNNNN- prefix convention.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DcmdirInfoMghOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMDIR_INFO_MGH_METADATA)
    params = dcmdir_info_mgh_params(
        dicomdir=dicomdir,
        unpackdir=unpackdir,
        version=version,
        help_=help_,
        nopre=nopre,
    )
    return dcmdir_info_mgh_execute(params, execution)


__all__ = [
    "DCMDIR_INFO_MGH_METADATA",
    "DcmdirInfoMghOutputs",
    "DcmdirInfoMghParameters",
    "dcmdir_info_mgh",
    "dcmdir_info_mgh_params",
]
