# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANNOTATION_RESAMPLE_METADATA = Metadata(
    id="2c6cadad264ac128829e478e77f82b0c84d405b7.boutiques",
    name="annotation-resample",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


AnnotationResampleSurfacePairParameters = typing.TypedDict('AnnotationResampleSurfacePairParameters', {
    "__STYXTYPE__": typing.Literal["surface_pair"],
    "source_surface": InputPathType,
    "target_surface": InputPathType,
})


AnnotationResampleParameters = typing.TypedDict('AnnotationResampleParameters', {
    "__STYXTYPE__": typing.Literal["annotation-resample"],
    "annotation_in": InputPathType,
    "annotation_out": str,
    "surface_pair": typing.NotRequired[list[AnnotationResampleSurfacePairParameters] | None],
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
        "annotation-resample": annotation_resample_cargs,
        "surface_pair": annotation_resample_surface_pair_cargs,
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


def annotation_resample_surface_pair_params(
    source_surface: InputPathType,
    target_surface: InputPathType,
) -> AnnotationResampleSurfacePairParameters:
    """
    Build parameters.
    
    Args:
        source_surface: the midthickness surface of the current mesh the\
            annotations use.
        target_surface: the midthickness surface of the mesh the annotations\
            should be transferred to.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface_pair",
        "source_surface": source_surface,
        "target_surface": target_surface,
    }
    return params


def annotation_resample_surface_pair_cargs(
    params: AnnotationResampleSurfacePairParameters,
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
    cargs.append("-surface-pair")
    cargs.append(execution.input_file(params.get("source_surface")))
    cargs.append(execution.input_file(params.get("target_surface")))
    return cargs


class AnnotationResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `annotation_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def annotation_resample_params(
    annotation_in: InputPathType,
    annotation_out: str,
    surface_pair: list[AnnotationResampleSurfacePairParameters] | None = None,
) -> AnnotationResampleParameters:
    """
    Build parameters.
    
    Args:
        annotation_in: the annotation file to resample.
        annotation_out: name of resampled annotation file.
        surface_pair: pair of surfaces for resampling surface annotations for\
            one structure.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "annotation-resample",
        "annotation_in": annotation_in,
        "annotation_out": annotation_out,
    }
    if surface_pair is not None:
        params["surface_pair"] = surface_pair
    return params


def annotation_resample_cargs(
    params: AnnotationResampleParameters,
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
    cargs.append("wb_command")
    cargs.append("-annotation-resample")
    cargs.append(execution.input_file(params.get("annotation_in")))
    cargs.append(params.get("annotation_out"))
    if params.get("surface_pair") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("surface_pair")] for a in c])
    return cargs


def annotation_resample_outputs(
    params: AnnotationResampleParameters,
    execution: Execution,
) -> AnnotationResampleOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AnnotationResampleOutputs(
        root=execution.output_file("."),
    )
    return ret


def annotation_resample_execute(
    params: AnnotationResampleParameters,
    execution: Execution,
) -> AnnotationResampleOutputs:
    """
    Resample an annotation file to different meshes.
    
    Resample an annotation file from the source mesh to the target mesh.
    
    Only annotations in surface space are modified, no changes are made to
    annotations in other spaces. The -surface-pair option may be repeated for
    additional structures used by surface space annotations.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AnnotationResampleOutputs`).
    """
    params = execution.params(params)
    cargs = annotation_resample_cargs(params, execution)
    ret = annotation_resample_outputs(params, execution)
    execution.run(cargs)
    return ret


def annotation_resample(
    annotation_in: InputPathType,
    annotation_out: str,
    surface_pair: list[AnnotationResampleSurfacePairParameters] | None = None,
    runner: Runner | None = None,
) -> AnnotationResampleOutputs:
    """
    Resample an annotation file to different meshes.
    
    Resample an annotation file from the source mesh to the target mesh.
    
    Only annotations in surface space are modified, no changes are made to
    annotations in other spaces. The -surface-pair option may be repeated for
    additional structures used by surface space annotations.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        annotation_in: the annotation file to resample.
        annotation_out: name of resampled annotation file.
        surface_pair: pair of surfaces for resampling surface annotations for\
            one structure.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AnnotationResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANNOTATION_RESAMPLE_METADATA)
    params = annotation_resample_params(
        annotation_in=annotation_in,
        annotation_out=annotation_out,
        surface_pair=surface_pair,
    )
    return annotation_resample_execute(params, execution)


__all__ = [
    "ANNOTATION_RESAMPLE_METADATA",
    "AnnotationResampleOutputs",
    "AnnotationResampleParameters",
    "AnnotationResampleSurfacePairParameters",
    "annotation_resample",
    "annotation_resample_params",
    "annotation_resample_surface_pair_params",
]
