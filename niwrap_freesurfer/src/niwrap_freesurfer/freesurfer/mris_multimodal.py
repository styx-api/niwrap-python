# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_MULTIMODAL_METADATA = Metadata(
    id="41d6bb30b581761db606adc285367bb0716e55ee.boutiques",
    name="mris_multimodal",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisMultimodalParameters = typing.TypedDict('MrisMultimodalParameters', {
    "__STYX_TYPE__": typing.Literal["mris_multimodal"],
    "input_surface": InputPathType,
    "target_surface": InputPathType,
    "output_surface": str,
    "fill_holes": bool,
    "curvature": bool,
    "thickness": bool,
    "annotation_output": str,
    "overlay_output": str,
    "csv_output": str,
    "vtk_output": bool,
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
        "mris_multimodal": mris_multimodal_cargs,
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
        "mris_multimodal": mris_multimodal_outputs,
    }.get(t)


class MrisMultimodalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_multimodal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    processed_output_surface: OutputPathType
    """Processed output surface file."""
    annotation_output_file: OutputPathType
    """Output file containing annotation data."""
    overlay_output_file: OutputPathType
    """Output file containing overlay data."""
    csv_output_file: OutputPathType
    """Output CSV file."""


def mris_multimodal_params(
    input_surface: InputPathType,
    target_surface: InputPathType,
    output_surface: str,
    annotation_output: str,
    overlay_output: str,
    csv_output: str,
    fill_holes: bool = False,
    curvature: bool = False,
    thickness: bool = False,
    vtk_output: bool = False,
) -> MrisMultimodalParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file.
        target_surface: Target surface file.
        output_surface: Output surface file.
        annotation_output: Output file for annotation data.
        overlay_output: Output file for overlay data.
        csv_output: Output CSV file.
        fill_holes: Flag to fill holes in the surface.
        curvature: Flag to process curvature data.
        thickness: Flag to process thickness data.
        vtk_output: Flag to output VTK file format.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_multimodal",
        "input_surface": input_surface,
        "target_surface": target_surface,
        "output_surface": output_surface,
        "fill_holes": fill_holes,
        "curvature": curvature,
        "thickness": thickness,
        "annotation_output": annotation_output,
        "overlay_output": overlay_output,
        "csv_output": csv_output,
        "vtk_output": vtk_output,
    }
    return params


def mris_multimodal_cargs(
    params: MrisMultimodalParameters,
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
    cargs.append("mris_multimodal")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_surface"))
    ])
    cargs.extend([
        "-t",
        execution.input_file(params.get("target_surface"))
    ])
    cargs.extend([
        "-o",
        params.get("output_surface")
    ])
    if params.get("fill_holes"):
        cargs.append("-fillHoles")
    if params.get("curvature"):
        cargs.append("--curvature")
    if params.get("thickness"):
        cargs.append("--thickness")
    cargs.extend([
        "-a",
        params.get("annotation_output")
    ])
    cargs.extend([
        "-v",
        params.get("overlay_output")
    ])
    cargs.extend([
        "-c",
        params.get("csv_output")
    ])
    if params.get("vtk_output"):
        cargs.append("-vtk")
    return cargs


def mris_multimodal_outputs(
    params: MrisMultimodalParameters,
    execution: Execution,
) -> MrisMultimodalOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMultimodalOutputs(
        root=execution.output_file("."),
        processed_output_surface=execution.output_file(params.get("output_surface")),
        annotation_output_file=execution.output_file(params.get("annotation_output")),
        overlay_output_file=execution.output_file(params.get("overlay_output")),
        csv_output_file=execution.output_file(params.get("csv_output")),
    )
    return ret


def mris_multimodal_execute(
    params: MrisMultimodalParameters,
    execution: Execution,
) -> MrisMultimodalOutputs:
    """
    A FreeSurfer tool for processing multimodal surface data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMultimodalOutputs`).
    """
    params = execution.params(params)
    cargs = mris_multimodal_cargs(params, execution)
    ret = mris_multimodal_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_multimodal(
    input_surface: InputPathType,
    target_surface: InputPathType,
    output_surface: str,
    annotation_output: str,
    overlay_output: str,
    csv_output: str,
    fill_holes: bool = False,
    curvature: bool = False,
    thickness: bool = False,
    vtk_output: bool = False,
    runner: Runner | None = None,
) -> MrisMultimodalOutputs:
    """
    A FreeSurfer tool for processing multimodal surface data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        target_surface: Target surface file.
        output_surface: Output surface file.
        annotation_output: Output file for annotation data.
        overlay_output: Output file for overlay data.
        csv_output: Output CSV file.
        fill_holes: Flag to fill holes in the surface.
        curvature: Flag to process curvature data.
        thickness: Flag to process thickness data.
        vtk_output: Flag to output VTK file format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMultimodalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MULTIMODAL_METADATA)
    params = mris_multimodal_params(
        input_surface=input_surface,
        target_surface=target_surface,
        output_surface=output_surface,
        fill_holes=fill_holes,
        curvature=curvature,
        thickness=thickness,
        annotation_output=annotation_output,
        overlay_output=overlay_output,
        csv_output=csv_output,
        vtk_output=vtk_output,
    )
    return mris_multimodal_execute(params, execution)


__all__ = [
    "MRIS_MULTIMODAL_METADATA",
    "MrisMultimodalOutputs",
    "MrisMultimodalParameters",
    "mris_multimodal",
    "mris_multimodal_params",
]
