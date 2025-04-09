# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_LABEL_ADJACENCY_METADATA = Metadata(
    id="5441d34fe7da5e1d9fb8b7ac840958f08da38c7b.boutiques",
    name="cifti-label-adjacency",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


CiftiLabelAdjacencyParameters = typing.TypedDict('CiftiLabelAdjacencyParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-label-adjacency"],
    "label_in": InputPathType,
    "adjacency_out": str,
    "opt_left_surface_surface": typing.NotRequired[InputPathType | None],
    "opt_right_surface_surface": typing.NotRequired[InputPathType | None],
    "opt_cerebellum_surface_surface": typing.NotRequired[InputPathType | None],
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
        "cifti-label-adjacency": cifti_label_adjacency_cargs,
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
        "cifti-label-adjacency": cifti_label_adjacency_outputs,
    }.get(t)


class CiftiLabelAdjacencyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_adjacency(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    adjacency_out: OutputPathType
    """the output cifti pconn adjacency matrix"""


def cifti_label_adjacency_params(
    label_in: InputPathType,
    adjacency_out: str,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
) -> CiftiLabelAdjacencyParameters:
    """
    Build parameters.
    
    Args:
        label_in: the input cifti label file.
        adjacency_out: the output cifti pconn adjacency matrix.
        opt_left_surface_surface: specify the left surface to use: the left\
            surface file.
        opt_right_surface_surface: specify the right surface to use: the right\
            surface file.
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:\
            the cerebellum surface file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-label-adjacency",
        "label_in": label_in,
        "adjacency_out": adjacency_out,
    }
    if opt_left_surface_surface is not None:
        params["opt_left_surface_surface"] = opt_left_surface_surface
    if opt_right_surface_surface is not None:
        params["opt_right_surface_surface"] = opt_right_surface_surface
    if opt_cerebellum_surface_surface is not None:
        params["opt_cerebellum_surface_surface"] = opt_cerebellum_surface_surface
    return params


def cifti_label_adjacency_cargs(
    params: CiftiLabelAdjacencyParameters,
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
    cargs.append("-cifti-label-adjacency")
    cargs.append(execution.input_file(params.get("label_in")))
    cargs.append(params.get("adjacency_out"))
    if params.get("opt_left_surface_surface") is not None:
        cargs.extend([
            "-left-surface",
            execution.input_file(params.get("opt_left_surface_surface"))
        ])
    if params.get("opt_right_surface_surface") is not None:
        cargs.extend([
            "-right-surface",
            execution.input_file(params.get("opt_right_surface_surface"))
        ])
    if params.get("opt_cerebellum_surface_surface") is not None:
        cargs.extend([
            "-cerebellum-surface",
            execution.input_file(params.get("opt_cerebellum_surface_surface"))
        ])
    return cargs


def cifti_label_adjacency_outputs(
    params: CiftiLabelAdjacencyParameters,
    execution: Execution,
) -> CiftiLabelAdjacencyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiLabelAdjacencyOutputs(
        root=execution.output_file("."),
        adjacency_out=execution.output_file(params.get("adjacency_out")),
    )
    return ret


def cifti_label_adjacency_execute(
    params: CiftiLabelAdjacencyParameters,
    execution: Execution,
) -> CiftiLabelAdjacencyOutputs:
    """
    Make adjacency matrix of a cifti label file.
    
    Find face-adjacent voxels and connected vertices that have different label
    values, and count them for each pair. Put the resulting counts into a
    parcellated connectivity file, with the diagonal being zero. This gives a
    rough estimate of how long or expansive the border between two labels is.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelAdjacencyOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_label_adjacency_cargs(params, execution)
    ret = cifti_label_adjacency_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_label_adjacency(
    label_in: InputPathType,
    adjacency_out: str,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
    runner: Runner | None = None,
) -> CiftiLabelAdjacencyOutputs:
    """
    Make adjacency matrix of a cifti label file.
    
    Find face-adjacent voxels and connected vertices that have different label
    values, and count them for each pair. Put the resulting counts into a
    parcellated connectivity file, with the diagonal being zero. This gives a
    rough estimate of how long or expansive the border between two labels is.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input cifti label file.
        adjacency_out: the output cifti pconn adjacency matrix.
        opt_left_surface_surface: specify the left surface to use: the left\
            surface file.
        opt_right_surface_surface: specify the right surface to use: the right\
            surface file.
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:\
            the cerebellum surface file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelAdjacencyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_LABEL_ADJACENCY_METADATA)
    params = cifti_label_adjacency_params(
        label_in=label_in,
        adjacency_out=adjacency_out,
        opt_left_surface_surface=opt_left_surface_surface,
        opt_right_surface_surface=opt_right_surface_surface,
        opt_cerebellum_surface_surface=opt_cerebellum_surface_surface,
    )
    return cifti_label_adjacency_execute(params, execution)


__all__ = [
    "CIFTI_LABEL_ADJACENCY_METADATA",
    "CiftiLabelAdjacencyOutputs",
    "CiftiLabelAdjacencyParameters",
    "cifti_label_adjacency",
    "cifti_label_adjacency_params",
]
