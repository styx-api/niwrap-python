# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_CNR_METADATA = Metadata(
    id="34e4848716ab0ea4fe90a1336b47fb8b0d5d00d0.boutiques",
    name="mri_cnr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriCnrParameters = typing.TypedDict('MriCnrParameters', {
    "__STYXTYPE__": typing.Literal["mri_cnr"],
    "surf_dir": str,
    "volume_files": list[InputPathType],
    "slope": typing.NotRequired[list[str] | None],
    "logfile": typing.NotRequired[str | None],
    "labels": typing.NotRequired[list[str] | None],
    "print_total_cnr": bool,
    "version_flag": bool,
    "help_flag": bool,
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
        "mri_cnr": mri_cnr_cargs,
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


class MriCnrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_cnr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_cnr_params(
    surf_dir: str,
    volume_files: list[InputPathType],
    slope: list[str] | None = None,
    logfile: str | None = None,
    labels: list[str] | None = None,
    print_total_cnr: bool = False,
    version_flag: bool = False,
    help_flag: bool = False,
) -> MriCnrParameters:
    """
    Build parameters.
    
    Args:
        surf_dir: Directory containing surface data.
        volume_files: Volumes to process.
        slope: Compute slope and write to files labeled with slope_fname.\
            Requires four additional values: dist_in, dist_out, step_in, and\
            step_out.
        logfile: Log CNR to specified logfile. Will contain 8 values in a\
            specific order: gray_white_cnr, gray_csf_cnr, white_mean, gray_mean,\
            csf_mean, sqrt(white_var), sqrt(gray_var), sqrt(csf_var).
        labels: Read hemisphere labels from specified left and right hemisphere\
            files.
        print_total_cnr: Print only the total CNR to stdout.
        version_flag: Print software version information and quit.
        help_flag: Print usage information and quit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_cnr",
        "surf_dir": surf_dir,
        "volume_files": volume_files,
        "print_total_cnr": print_total_cnr,
        "version_flag": version_flag,
        "help_flag": help_flag,
    }
    if slope is not None:
        params["slope"] = slope
    if logfile is not None:
        params["logfile"] = logfile
    if labels is not None:
        params["labels"] = labels
    return params


def mri_cnr_cargs(
    params: MriCnrParameters,
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
    cargs.append("mri_cnr")
    cargs.append(params.get("surf_dir"))
    cargs.extend([execution.input_file(f) for f in params.get("volume_files")])
    if params.get("slope") is not None:
        cargs.extend([
            "-s",
            *params.get("slope")
        ])
    if params.get("logfile") is not None:
        cargs.extend([
            "-l",
            params.get("logfile")
        ])
    if params.get("labels") is not None:
        cargs.extend([
            "label",
            *params.get("labels")
        ])
    if params.get("print_total_cnr"):
        cargs.append("-t")
    if params.get("version_flag"):
        cargs.append("-version")
    if params.get("help_flag"):
        cargs.append("-help")
    return cargs


def mri_cnr_outputs(
    params: MriCnrParameters,
    execution: Execution,
) -> MriCnrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCnrOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_cnr_execute(
    params: MriCnrParameters,
    execution: Execution,
) -> MriCnrOutputs:
    """
    Compute the gray/white/csf contrast-to-noise ratio for volumes using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCnrOutputs`).
    """
    params = execution.params(params)
    cargs = mri_cnr_cargs(params, execution)
    ret = mri_cnr_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_cnr(
    surf_dir: str,
    volume_files: list[InputPathType],
    slope: list[str] | None = None,
    logfile: str | None = None,
    labels: list[str] | None = None,
    print_total_cnr: bool = False,
    version_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> MriCnrOutputs:
    """
    Compute the gray/white/csf contrast-to-noise ratio for volumes using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surf_dir: Directory containing surface data.
        volume_files: Volumes to process.
        slope: Compute slope and write to files labeled with slope_fname.\
            Requires four additional values: dist_in, dist_out, step_in, and\
            step_out.
        logfile: Log CNR to specified logfile. Will contain 8 values in a\
            specific order: gray_white_cnr, gray_csf_cnr, white_mean, gray_mean,\
            csf_mean, sqrt(white_var), sqrt(gray_var), sqrt(csf_var).
        labels: Read hemisphere labels from specified left and right hemisphere\
            files.
        print_total_cnr: Print only the total CNR to stdout.
        version_flag: Print software version information and quit.
        help_flag: Print usage information and quit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCnrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CNR_METADATA)
    params = mri_cnr_params(
        surf_dir=surf_dir,
        volume_files=volume_files,
        slope=slope,
        logfile=logfile,
        labels=labels,
        print_total_cnr=print_total_cnr,
        version_flag=version_flag,
        help_flag=help_flag,
    )
    return mri_cnr_execute(params, execution)


__all__ = [
    "MRI_CNR_METADATA",
    "MriCnrOutputs",
    "MriCnrParameters",
    "mri_cnr",
    "mri_cnr_params",
]
