# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_COMPUTE_LAYER_INTENSITIES_METADATA = Metadata(
    id="f24960e9a74b3ae18e3affaefde83e7e04cb8a2b.boutiques",
    name="mris_compute_layer_intensities",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisComputeLayerIntensitiesParameters = typing.TypedDict('MrisComputeLayerIntensitiesParameters', {
    "__STYX_TYPE__": typing.Literal["mris_compute_layer_intensities"],
    "input_intensity_volume": InputPathType,
    "layer_volume_fractions_file": InputPathType,
    "input_surface": InputPathType,
    "output_overlay": str,
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
        "mris_compute_layer_intensities": mris_compute_layer_intensities_cargs,
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
        "mris_compute_layer_intensities": mris_compute_layer_intensities_outputs,
    }.get(t)


class MrisComputeLayerIntensitiesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_compute_layer_intensities(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_overlay_file: OutputPathType
    """The output overlay file generated by the tool."""


def mris_compute_layer_intensities_params(
    input_intensity_volume: InputPathType,
    layer_volume_fractions_file: InputPathType,
    input_surface: InputPathType,
    output_overlay: str,
) -> MrisComputeLayerIntensitiesParameters:
    """
    Build parameters.
    
    Args:
        input_intensity_volume: The input intensity volume file.
        layer_volume_fractions_file: The layer volume fractions file.
        input_surface: The input surface file for layer intensity computation.
        output_overlay: The output file where the overlay will be saved.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_compute_layer_intensities",
        "input_intensity_volume": input_intensity_volume,
        "layer_volume_fractions_file": layer_volume_fractions_file,
        "input_surface": input_surface,
        "output_overlay": output_overlay,
    }
    return params


def mris_compute_layer_intensities_cargs(
    params: MrisComputeLayerIntensitiesParameters,
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
    cargs.append("mris_compute_layer_intensities")
    cargs.append(execution.input_file(params.get("input_intensity_volume")))
    cargs.append(execution.input_file(params.get("layer_volume_fractions_file")))
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(params.get("output_overlay"))
    return cargs


def mris_compute_layer_intensities_outputs(
    params: MrisComputeLayerIntensitiesParameters,
    execution: Execution,
) -> MrisComputeLayerIntensitiesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisComputeLayerIntensitiesOutputs(
        root=execution.output_file("."),
        output_overlay_file=execution.output_file(params.get("output_overlay")),
    )
    return ret


def mris_compute_layer_intensities_execute(
    params: MrisComputeLayerIntensitiesParameters,
    execution: Execution,
) -> MrisComputeLayerIntensitiesOutputs:
    """
    Computes intensity overlays for specified cortical layers based on input volumes
    and surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisComputeLayerIntensitiesOutputs`).
    """
    params = execution.params(params)
    cargs = mris_compute_layer_intensities_cargs(params, execution)
    ret = mris_compute_layer_intensities_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_compute_layer_intensities(
    input_intensity_volume: InputPathType,
    layer_volume_fractions_file: InputPathType,
    input_surface: InputPathType,
    output_overlay: str,
    runner: Runner | None = None,
) -> MrisComputeLayerIntensitiesOutputs:
    """
    Computes intensity overlays for specified cortical layers based on input volumes
    and surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_intensity_volume: The input intensity volume file.
        layer_volume_fractions_file: The layer volume fractions file.
        input_surface: The input surface file for layer intensity computation.
        output_overlay: The output file where the overlay will be saved.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisComputeLayerIntensitiesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_COMPUTE_LAYER_INTENSITIES_METADATA)
    params = mris_compute_layer_intensities_params(
        input_intensity_volume=input_intensity_volume,
        layer_volume_fractions_file=layer_volume_fractions_file,
        input_surface=input_surface,
        output_overlay=output_overlay,
    )
    return mris_compute_layer_intensities_execute(params, execution)


__all__ = [
    "MRIS_COMPUTE_LAYER_INTENSITIES_METADATA",
    "MrisComputeLayerIntensitiesOutputs",
    "MrisComputeLayerIntensitiesParameters",
    "mris_compute_layer_intensities",
    "mris_compute_layer_intensities_params",
]
