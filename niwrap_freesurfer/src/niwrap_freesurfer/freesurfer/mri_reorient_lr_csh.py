# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_REORIENT_LR_CSH_METADATA = Metadata(
    id="05322ddfbba756994657c542f9080b8197d048b6.boutiques",
    name="mri_reorient_LR.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriReorientLrCshParameters = typing.TypedDict('MriReorientLrCshParameters', {
    "__STYXTYPE__": typing.Literal["mri_reorient_LR.csh"],
    "input_vol": InputPathType,
    "output_vol": str,
    "display_result": bool,
    "clean_files": bool,
    "output_registration": bool,
    "version": bool,
    "help": bool,
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
        "mri_reorient_LR.csh": mri_reorient_lr_csh_cargs,
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
        "mri_reorient_LR.csh": mri_reorient_lr_csh_outputs,
    }.get(t)


class MriReorientLrCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_reorient_lr_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reoriented_vol: OutputPathType
    """Reoriented volume"""


def mri_reorient_lr_csh_params(
    input_vol: InputPathType,
    output_vol: str,
    display_result: bool = False,
    clean_files: bool = False,
    output_registration: bool = False,
    version: bool = False,
    help_: bool = False,
) -> MriReorientLrCshParameters:
    """
    Build parameters.
    
    Args:
        input_vol: Input file to be reoriented.
        output_vol: Reoriented input file.
        display_result: Display registration result using FreeView.
        clean_files: Delete all auxiliary and registration files.
        output_registration: Write out the registration file that is applied to\
            the reoriented input file (fslmat or lta).
        version: Print version and exit.
        help_: Print help and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_reorient_LR.csh",
        "input_vol": input_vol,
        "output_vol": output_vol,
        "display_result": display_result,
        "clean_files": clean_files,
        "output_registration": output_registration,
        "version": version,
        "help": help_,
    }
    return params


def mri_reorient_lr_csh_cargs(
    params: MriReorientLrCshParameters,
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
    cargs.append("mri_reorient_LR.csh")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_vol"))
    ])
    cargs.extend([
        "--o",
        params.get("output_vol")
    ])
    if params.get("display_result"):
        cargs.append("--disp")
    if params.get("clean_files"):
        cargs.append("--clean")
    if params.get("output_registration"):
        cargs.append("--outreg")
    if params.get("version"):
        cargs.append("--version")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def mri_reorient_lr_csh_outputs(
    params: MriReorientLrCshParameters,
    execution: Execution,
) -> MriReorientLrCshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriReorientLrCshOutputs(
        root=execution.output_file("."),
        reoriented_vol=execution.output_file(params.get("output_vol")),
    )
    return ret


def mri_reorient_lr_csh_execute(
    params: MriReorientLrCshParameters,
    execution: Execution,
) -> MriReorientLrCshOutputs:
    """
    A script to reorient MRI volumes from left-right orientation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriReorientLrCshOutputs`).
    """
    params = execution.params(params)
    cargs = mri_reorient_lr_csh_cargs(params, execution)
    ret = mri_reorient_lr_csh_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_reorient_lr_csh(
    input_vol: InputPathType,
    output_vol: str,
    display_result: bool = False,
    clean_files: bool = False,
    output_registration: bool = False,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriReorientLrCshOutputs:
    """
    A script to reorient MRI volumes from left-right orientation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_vol: Input file to be reoriented.
        output_vol: Reoriented input file.
        display_result: Display registration result using FreeView.
        clean_files: Delete all auxiliary and registration files.
        output_registration: Write out the registration file that is applied to\
            the reoriented input file (fslmat or lta).
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriReorientLrCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_REORIENT_LR_CSH_METADATA)
    params = mri_reorient_lr_csh_params(
        input_vol=input_vol,
        output_vol=output_vol,
        display_result=display_result,
        clean_files=clean_files,
        output_registration=output_registration,
        version=version,
        help_=help_,
    )
    return mri_reorient_lr_csh_execute(params, execution)


__all__ = [
    "MRI_REORIENT_LR_CSH_METADATA",
    "MriReorientLrCshOutputs",
    "MriReorientLrCshParameters",
    "mri_reorient_lr_csh",
    "mri_reorient_lr_csh_params",
]
