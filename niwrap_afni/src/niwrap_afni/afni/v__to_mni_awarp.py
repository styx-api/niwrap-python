# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__TO_MNI_AWARP_METADATA = Metadata(
    id="93b77f09cd479bf6a950c0693a066eccc0f62501.boutiques",
    name="@toMNI_Awarp",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VToMniAwarpParameters = typing.TypedDict('VToMniAwarpParameters', {
    "__STYX_TYPE__": typing.Literal["@toMNI_Awarp"],
    "directory": str,
    "datasets": list[InputPathType],
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
        "@toMNI_Awarp": v__to_mni_awarp_cargs,
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
        "@toMNI_Awarp": v__to_mni_awarp_outputs,
    }.get(t)


class VToMniAwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__to_mni_awarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_datasets: OutputPathType
    """The transformed datasets in 1x1x1 mm MNI space."""


def v__to_mni_awarp_params(
    directory: str,
    datasets: list[InputPathType],
) -> VToMniAwarpParameters:
    """
    Build parameters.
    
    Args:
        directory: Name of the directory to be created where results will be\
            stored.
        datasets: List of datasets to be transformed.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@toMNI_Awarp",
        "directory": directory,
        "datasets": datasets,
    }
    return params


def v__to_mni_awarp_cargs(
    params: VToMniAwarpParameters,
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
    cargs.append("@toMNI_Awarp")
    cargs.append(params.get("directory"))
    cargs.extend([execution.input_file(f) for f in params.get("datasets")])
    return cargs


def v__to_mni_awarp_outputs(
    params: VToMniAwarpParameters,
    execution: Execution,
) -> VToMniAwarpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VToMniAwarpOutputs(
        root=execution.output_file("."),
        output_datasets=execution.output_file(params.get("directory") + "/*"),
    )
    return ret


def v__to_mni_awarp_execute(
    params: VToMniAwarpParameters,
    execution: Execution,
) -> VToMniAwarpOutputs:
    """
    Transforms skull-stripped datasets to 1x1x1 mm MNI space using an affine
    transformation.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VToMniAwarpOutputs`).
    """
    params = execution.params(params)
    cargs = v__to_mni_awarp_cargs(params, execution)
    ret = v__to_mni_awarp_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__to_mni_awarp(
    directory: str,
    datasets: list[InputPathType],
    runner: Runner | None = None,
) -> VToMniAwarpOutputs:
    """
    Transforms skull-stripped datasets to 1x1x1 mm MNI space using an affine
    transformation.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        directory: Name of the directory to be created where results will be\
            stored.
        datasets: List of datasets to be transformed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VToMniAwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__TO_MNI_AWARP_METADATA)
    params = v__to_mni_awarp_params(
        directory=directory,
        datasets=datasets,
    )
    return v__to_mni_awarp_execute(params, execution)


__all__ = [
    "VToMniAwarpOutputs",
    "VToMniAwarpParameters",
    "V__TO_MNI_AWARP_METADATA",
    "v__to_mni_awarp",
    "v__to_mni_awarp_params",
]
