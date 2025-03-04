# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__ISO_MASKS_METADATA = Metadata(
    id="efb13b19016645aff7a7273058c6f68edcfc682d.boutiques",
    name="@IsoMasks",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VIsoMasksParameters = typing.TypedDict('VIsoMasksParameters', {
    "__STYX_TYPE__": typing.Literal["@IsoMasks"],
    "input_dataset": InputPathType,
    "isovals": typing.NotRequired[list[float] | None],
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
        "@IsoMasks": v__iso_masks_cargs,
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


class VIsoMasksOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__iso_masks(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__iso_masks_params(
    input_dataset: InputPathType,
    isovals: list[float] | None = None,
) -> VIsoMasksParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset for creating isosurfaces.
        isovals: Isovalue thresholds for creating isosurfaces.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@IsoMasks",
        "input_dataset": input_dataset,
    }
    if isovals is not None:
        params["isovals"] = isovals
    return params


def v__iso_masks_cargs(
    params: VIsoMasksParameters,
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
    cargs.append("@IsoMasks")
    cargs.extend([
        "-mask",
        execution.input_file(params.get("input_dataset"))
    ])
    if params.get("isovals") is not None:
        cargs.extend(map(str, params.get("isovals")))
    return cargs


def v__iso_masks_outputs(
    params: VIsoMasksParameters,
    execution: Execution,
) -> VIsoMasksOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VIsoMasksOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__iso_masks_execute(
    params: VIsoMasksParameters,
    execution: Execution,
) -> VIsoMasksOutputs:
    """
    Creates isosurfaces from isovolume envelopes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VIsoMasksOutputs`).
    """
    params = execution.params(params)
    cargs = v__iso_masks_cargs(params, execution)
    ret = v__iso_masks_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__iso_masks(
    input_dataset: InputPathType,
    isovals: list[float] | None = None,
    runner: Runner | None = None,
) -> VIsoMasksOutputs:
    """
    Creates isosurfaces from isovolume envelopes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset for creating isosurfaces.
        isovals: Isovalue thresholds for creating isosurfaces.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VIsoMasksOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__ISO_MASKS_METADATA)
    params = v__iso_masks_params(
        input_dataset=input_dataset,
        isovals=isovals,
    )
    return v__iso_masks_execute(params, execution)


__all__ = [
    "VIsoMasksOutputs",
    "VIsoMasksParameters",
    "V__ISO_MASKS_METADATA",
    "v__iso_masks",
    "v__iso_masks_params",
]
