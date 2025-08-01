# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__GET_AFNI_DIMS_METADATA = Metadata(
    id="79e1fb9221be43e2a30199228c1691b4a01fb471.boutiques",
    name="@GetAfniDims",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VGetAfniDimsParameters = typing.TypedDict('VGetAfniDimsParameters', {
    "__STYXTYPE__": typing.Literal["@GetAfniDims"],
    "input_dset": InputPathType,
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
        "@GetAfniDims": v__get_afni_dims_cargs,
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
        "@GetAfniDims": v__get_afni_dims_outputs,
    }.get(t)


class VGetAfniDimsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__get_afni_dims(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dims_output: OutputPathType
    """Text file containing the dimensions of the input dataset"""


def v__get_afni_dims_params(
    input_dset: InputPathType,
) -> VGetAfniDimsParameters:
    """
    Build parameters.
    
    Args:
        input_dset: Input AFNI dataset.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@GetAfniDims",
        "input_dset": input_dset,
    }
    return params


def v__get_afni_dims_cargs(
    params: VGetAfniDimsParameters,
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
    cargs.append("@GetAfniDims")
    cargs.append(execution.input_file(params.get("input_dset")))
    return cargs


def v__get_afni_dims_outputs(
    params: VGetAfniDimsParameters,
    execution: Execution,
) -> VGetAfniDimsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VGetAfniDimsOutputs(
        root=execution.output_file("."),
        dims_output=execution.output_file("dims_output.txt"),
    )
    return ret


def v__get_afni_dims_execute(
    params: VGetAfniDimsParameters,
    execution: Execution,
) -> VGetAfniDimsOutputs:
    """
    A utility tool to return dimensions of AFNI dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VGetAfniDimsOutputs`).
    """
    params = execution.params(params)
    cargs = v__get_afni_dims_cargs(params, execution)
    ret = v__get_afni_dims_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__get_afni_dims(
    input_dset: InputPathType,
    runner: Runner | None = None,
) -> VGetAfniDimsOutputs:
    """
    A utility tool to return dimensions of AFNI dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dset: Input AFNI dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGetAfniDimsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GET_AFNI_DIMS_METADATA)
    params = v__get_afni_dims_params(
        input_dset=input_dset,
    )
    return v__get_afni_dims_execute(params, execution)


__all__ = [
    "VGetAfniDimsOutputs",
    "VGetAfniDimsParameters",
    "V__GET_AFNI_DIMS_METADATA",
    "v__get_afni_dims",
    "v__get_afni_dims_params",
]
