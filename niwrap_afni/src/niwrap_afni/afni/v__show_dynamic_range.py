# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__SHOW_DYNAMIC_RANGE_METADATA = Metadata(
    id="79a18236c270604039c67089fe05e4d75deeff40.boutiques",
    name="@ShowDynamicRange",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VShowDynamicRangeParameters = typing.TypedDict('VShowDynamicRangeParameters', {
    "__STYXTYPE__": typing.Literal["@ShowDynamicRange"],
    "infile": InputPathType,
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
        "@ShowDynamicRange": v__show_dynamic_range_cargs,
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
        "@ShowDynamicRange": v__show_dynamic_range_outputs,
    }.get(t)


class VShowDynamicRangeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__show_dynamic_range(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    minpercchange_file: OutputPathType
    """Dataset showing the percent signal change that an increment of 1
    digitized value in the time series corresponds to."""
    range_file: OutputPathType
    """Dataset showing the number of discrete levels used to represent the time
    series."""


def v__show_dynamic_range_params(
    infile: InputPathType,
) -> VShowDynamicRangeParameters:
    """
    Build parameters.
    
    Args:
        infile: Input EPI time series dataset (e.g. epi.nii.gz).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ShowDynamicRange",
        "infile": infile,
    }
    return params


def v__show_dynamic_range_cargs(
    params: VShowDynamicRangeParameters,
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
    cargs.append("@ShowDynamicRange")
    cargs.append(execution.input_file(params.get("infile")))
    return cargs


def v__show_dynamic_range_outputs(
    params: VShowDynamicRangeParameters,
    execution: Execution,
) -> VShowDynamicRangeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VShowDynamicRangeOutputs(
        root=execution.output_file("."),
        minpercchange_file=execution.output_file(pathlib.Path(params.get("infile")).name + "_minpercchange.nii.gz"),
        range_file=execution.output_file(pathlib.Path(params.get("infile")).name + ".range.nii.gz"),
    )
    return ret


def v__show_dynamic_range_execute(
    params: VShowDynamicRangeParameters,
    execution: Execution,
) -> VShowDynamicRangeOutputs:
    """
    The script checks the dynamic range of the time series data at locations inside
    the brain.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VShowDynamicRangeOutputs`).
    """
    params = execution.params(params)
    cargs = v__show_dynamic_range_cargs(params, execution)
    ret = v__show_dynamic_range_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__show_dynamic_range(
    infile: InputPathType,
    runner: Runner | None = None,
) -> VShowDynamicRangeOutputs:
    """
    The script checks the dynamic range of the time series data at locations inside
    the brain.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input EPI time series dataset (e.g. epi.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VShowDynamicRangeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SHOW_DYNAMIC_RANGE_METADATA)
    params = v__show_dynamic_range_params(
        infile=infile,
    )
    return v__show_dynamic_range_execute(params, execution)


__all__ = [
    "VShowDynamicRangeOutputs",
    "VShowDynamicRangeParameters",
    "V__SHOW_DYNAMIC_RANGE_METADATA",
    "v__show_dynamic_range",
    "v__show_dynamic_range_params",
]
