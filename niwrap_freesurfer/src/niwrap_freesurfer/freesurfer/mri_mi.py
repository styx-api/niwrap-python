# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_MI_METADATA = Metadata(
    id="ffac01dcb4fffeff7d686cc81a49d4b02727cd13.boutiques",
    name="mri_mi",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriMiParameters = typing.TypedDict('MriMiParameters', {
    "__STYXTYPE__": typing.Literal["mri_mi"],
    "input_file1": InputPathType,
    "input_file2": InputPathType,
    "bins": typing.NotRequired[str | None],
    "silent": bool,
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
        "mri_mi": mri_mi_cargs,
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


class MriMiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_mi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_mi_params(
    input_file1: InputPathType,
    input_file2: InputPathType,
    bins: str | None = None,
    silent: bool = False,
) -> MriMiParameters:
    """
    Build parameters.
    
    Args:
        input_file1: First input file name.
        input_file2: Second input file name.
        bins: Specifies the number of bins for the two input volumes. Default\
            is 64x64.
        silent: Write out only the final mutual information result.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_mi",
        "input_file1": input_file1,
        "input_file2": input_file2,
        "silent": silent,
    }
    if bins is not None:
        params["bins"] = bins
    return params


def mri_mi_cargs(
    params: MriMiParameters,
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
    cargs.append("mri_mi")
    cargs.append(execution.input_file(params.get("input_file1")))
    cargs.append(execution.input_file(params.get("input_file2")))
    if params.get("bins") is not None:
        cargs.extend([
            "--bins",
            params.get("bins")
        ])
    if params.get("silent"):
        cargs.append("--silent")
    return cargs


def mri_mi_outputs(
    params: MriMiParameters,
    execution: Execution,
) -> MriMiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriMiOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_mi_execute(
    params: MriMiParameters,
    execution: Execution,
) -> MriMiOutputs:
    """
    Computes mutual information (mi) between two input volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriMiOutputs`).
    """
    params = execution.params(params)
    cargs = mri_mi_cargs(params, execution)
    ret = mri_mi_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_mi(
    input_file1: InputPathType,
    input_file2: InputPathType,
    bins: str | None = None,
    silent: bool = False,
    runner: Runner | None = None,
) -> MriMiOutputs:
    """
    Computes mutual information (mi) between two input volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file1: First input file name.
        input_file2: Second input file name.
        bins: Specifies the number of bins for the two input volumes. Default\
            is 64x64.
        silent: Write out only the final mutual information result.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MI_METADATA)
    params = mri_mi_params(
        input_file1=input_file1,
        input_file2=input_file2,
        bins=bins,
        silent=silent,
    )
    return mri_mi_execute(params, execution)


__all__ = [
    "MRI_MI_METADATA",
    "MriMiOutputs",
    "MriMiParameters",
    "mri_mi",
    "mri_mi_params",
]
