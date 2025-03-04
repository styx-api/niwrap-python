# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__2DWARPER_METADATA = Metadata(
    id="00a0f14e7b2cc538eab7a1270968f6ba94c6c2e3.boutiques",
    name="@2dwarper",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V2dwarperParameters = typing.TypedDict('V2dwarperParameters', {
    "__STYX_TYPE__": typing.Literal["@2dwarper"],
    "input_dataset": InputPathType,
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
        "@2dwarper": v__2dwarper_cargs,
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
        "@2dwarper": v__2dwarper_outputs,
    }.get(t)


class V2dwarperOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__2dwarper(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Warped output image from the dataset"""


def v__2dwarper_params(
    input_dataset: InputPathType,
) -> V2dwarperParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset (e.g., image to be warped).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@2dwarper",
        "input_dataset": input_dataset,
    }
    return params


def v__2dwarper_cargs(
    params: V2dwarperParameters,
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
    cargs.append("@2dwarper")
    cargs.append(execution.input_file(params.get("input_dataset")))
    return cargs


def v__2dwarper_outputs(
    params: V2dwarperParameters,
    execution: Execution,
) -> V2dwarperOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V2dwarperOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("warped_output"),
    )
    return ret


def v__2dwarper_execute(
    params: V2dwarperParameters,
    execution: Execution,
) -> V2dwarperOutputs:
    """
    2D image warping tool.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V2dwarperOutputs`).
    """
    params = execution.params(params)
    cargs = v__2dwarper_cargs(params, execution)
    ret = v__2dwarper_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__2dwarper(
    input_dataset: InputPathType,
    runner: Runner | None = None,
) -> V2dwarperOutputs:
    """
    2D image warping tool.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset (e.g., image to be warped).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V2dwarperOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__2DWARPER_METADATA)
    params = v__2dwarper_params(
        input_dataset=input_dataset,
    )
    return v__2dwarper_execute(params, execution)


__all__ = [
    "V2dwarperOutputs",
    "V2dwarperParameters",
    "V__2DWARPER_METADATA",
    "v__2dwarper",
    "v__2dwarper_params",
]
