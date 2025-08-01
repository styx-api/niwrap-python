# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_COPY_VALUES_METADATA = Metadata(
    id="30903fcb07daf13b64da4d92816e79aa5d510758.boutiques",
    name="mri_copy_values",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriCopyValuesParameters = typing.TypedDict('MriCopyValuesParameters', {
    "__STYXTYPE__": typing.Literal["mri_copy_values"],
    "source_volume": InputPathType,
    "target_volume": InputPathType,
    "output_volume": str,
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
        "mri_copy_values": mri_copy_values_cargs,
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
        "mri_copy_values": mri_copy_values_outputs,
    }.get(t)


class MriCopyValuesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_copy_values(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output volume with copied values from source."""


def mri_copy_values_params(
    source_volume: InputPathType,
    target_volume: InputPathType,
    output_volume: str,
) -> MriCopyValuesParameters:
    """
    Build parameters.
    
    Args:
        source_volume: Source volume from which values are copied.
        target_volume: Target volume to which values are copied.
        output_volume: Output volume where the result will be stored.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_copy_values",
        "source_volume": source_volume,
        "target_volume": target_volume,
        "output_volume": output_volume,
    }
    return params


def mri_copy_values_cargs(
    params: MriCopyValuesParameters,
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
    cargs.append("mri_copy_values")
    cargs.append(execution.input_file(params.get("source_volume")))
    cargs.append(execution.input_file(params.get("target_volume")))
    cargs.append(params.get("output_volume"))
    return cargs


def mri_copy_values_outputs(
    params: MriCopyValuesParameters,
    execution: Execution,
) -> MriCopyValuesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCopyValuesOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_copy_values_execute(
    params: MriCopyValuesParameters,
    execution: Execution,
) -> MriCopyValuesOutputs:
    """
    No description.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCopyValuesOutputs`).
    """
    params = execution.params(params)
    cargs = mri_copy_values_cargs(params, execution)
    ret = mri_copy_values_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_copy_values(
    source_volume: InputPathType,
    target_volume: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> MriCopyValuesOutputs:
    """
    No description.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source_volume: Source volume from which values are copied.
        target_volume: Target volume to which values are copied.
        output_volume: Output volume where the result will be stored.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCopyValuesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COPY_VALUES_METADATA)
    params = mri_copy_values_params(
        source_volume=source_volume,
        target_volume=target_volume,
        output_volume=output_volume,
    )
    return mri_copy_values_execute(params, execution)


__all__ = [
    "MRI_COPY_VALUES_METADATA",
    "MriCopyValuesOutputs",
    "MriCopyValuesParameters",
    "mri_copy_values",
    "mri_copy_values_params",
]
