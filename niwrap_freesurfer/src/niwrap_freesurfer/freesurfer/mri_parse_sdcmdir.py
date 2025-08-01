# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_PARSE_SDCMDIR_METADATA = Metadata(
    id="da51e5d5af342cf720bb1d988d04c5f9f98e067a.boutiques",
    name="mri_parse_sdcmdir",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriParseSdcmdirParameters = typing.TypedDict('MriParseSdcmdirParameters', {
    "__STYXTYPE__": typing.Literal["mri_parse_sdcmdir"],
    "sdicomdir": str,
    "outfile": typing.NotRequired[str | None],
    "sortbyrun": bool,
    "summarize": bool,
    "dwi": bool,
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
        "mri_parse_sdcmdir": mri_parse_sdcmdir_cargs,
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
    }.get(t)


class MriParseSdcmdirOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_parse_sdcmdir(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_parse_sdcmdir_params(
    sdicomdir: str,
    outfile: str | None = None,
    sortbyrun: bool = False,
    summarize: bool = False,
    dwi: bool = False,
) -> MriParseSdcmdirParameters:
    """
    Build parameters.
    
    Args:
        sdicomdir: Path to Siemens DICOM directory.
        outfile: Name of a file to which the results will be printed. If\
            unspecified, the results will be printed to stdout.
        sortbyrun: Assign run numbers.
        summarize: Only print out info for run leaders.
        dwi: Try to read DWI params. Generally no need to.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_parse_sdcmdir",
        "sdicomdir": sdicomdir,
        "sortbyrun": sortbyrun,
        "summarize": summarize,
        "dwi": dwi,
    }
    if outfile is not None:
        params["outfile"] = outfile
    return params


def mri_parse_sdcmdir_cargs(
    params: MriParseSdcmdirParameters,
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
    cargs.append("mri_parse_sdcmdir")
    cargs.extend([
        "--d",
        params.get("sdicomdir")
    ])
    if params.get("outfile") is not None:
        cargs.extend([
            "--o",
            params.get("outfile")
        ])
    if params.get("sortbyrun"):
        cargs.append("--sortbyrun")
    if params.get("summarize"):
        cargs.append("--summarize")
    if params.get("dwi"):
        cargs.append("--dwi")
    return cargs


def mri_parse_sdcmdir_outputs(
    params: MriParseSdcmdirParameters,
    execution: Execution,
) -> MriParseSdcmdirOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriParseSdcmdirOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_parse_sdcmdir_execute(
    params: MriParseSdcmdirParameters,
    execution: Execution,
) -> MriParseSdcmdirOutputs:
    """
    This program parses the Siemens DICOM files in a given directory and prints out
    information about each file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriParseSdcmdirOutputs`).
    """
    params = execution.params(params)
    cargs = mri_parse_sdcmdir_cargs(params, execution)
    ret = mri_parse_sdcmdir_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_parse_sdcmdir(
    sdicomdir: str,
    outfile: str | None = None,
    sortbyrun: bool = False,
    summarize: bool = False,
    dwi: bool = False,
    runner: Runner | None = None,
) -> MriParseSdcmdirOutputs:
    """
    This program parses the Siemens DICOM files in a given directory and prints out
    information about each file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        sdicomdir: Path to Siemens DICOM directory.
        outfile: Name of a file to which the results will be printed. If\
            unspecified, the results will be printed to stdout.
        sortbyrun: Assign run numbers.
        summarize: Only print out info for run leaders.
        dwi: Try to read DWI params. Generally no need to.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriParseSdcmdirOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_PARSE_SDCMDIR_METADATA)
    params = mri_parse_sdcmdir_params(
        sdicomdir=sdicomdir,
        outfile=outfile,
        sortbyrun=sortbyrun,
        summarize=summarize,
        dwi=dwi,
    )
    return mri_parse_sdcmdir_execute(params, execution)


__all__ = [
    "MRI_PARSE_SDCMDIR_METADATA",
    "MriParseSdcmdirOutputs",
    "MriParseSdcmdirParameters",
    "mri_parse_sdcmdir",
    "mri_parse_sdcmdir_params",
]
