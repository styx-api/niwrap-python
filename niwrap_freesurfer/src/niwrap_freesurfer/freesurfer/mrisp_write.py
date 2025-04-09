# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRISP_WRITE_METADATA = Metadata(
    id="0ef5a849bb5e74469b12a33ed174cd4f7396c2f1.boutiques",
    name="mrisp_write",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrispWriteParameters = typing.TypedDict('MrispWriteParameters', {
    "__STYX_TYPE__": typing.Literal["mrisp_write"],
    "input_surface": InputPathType,
    "overlay_filename": InputPathType,
    "output_name": str,
    "subjects_dir": typing.NotRequired[str | None],
    "coords": typing.NotRequired[str | None],
    "average_curvature": typing.NotRequired[float | None],
    "correlation_matrix": typing.NotRequired[InputPathType | None],
    "scale_factor": typing.NotRequired[float | None],
    "normalize_curvature": bool,
    "verbose_vertex": typing.NotRequired[float | None],
    "write_diagnostics": bool,
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
        "mrisp_write": mrisp_write_cargs,
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
        "mrisp_write": mrisp_write_outputs,
    }.get(t)


class MrispWriteOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrisp_write(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """A file containing a surface-worth of per-vertex values saved in spherical
    coordinates."""


def mrisp_write_params(
    input_surface: InputPathType,
    overlay_filename: InputPathType,
    output_name: str,
    subjects_dir: str | None = None,
    coords: str | None = None,
    average_curvature: float | None = None,
    correlation_matrix: InputPathType | None = None,
    scale_factor: float | None = None,
    normalize_curvature: bool = False,
    verbose_vertex: float | None = None,
    write_diagnostics: bool = False,
) -> MrispWriteParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Full path to input surface.
        overlay_filename: Full path to the overlay to map.
        output_name: Output file name. Can be full path to a .tif or .mgz file.
        subjects_dir: Set SUBJECTS_DIR. Default: uses environment variable.
        coords: Treat overlay as a surface and write it into a 3 frame\
            parameterization.
        average_curvature: Average curvature patterns navgs times.
        correlation_matrix: Use the overlay to compute the correlation matrix\
            within the specified label.
        scale_factor: Scale factor to adjust resolution of the spherical map.
        normalize_curvature: Normalize curvature by variance.
        verbose_vertex: Invoke diagnostics for specified vertex number.
        write_diagnostics: Write some diagnostics.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mrisp_write",
        "input_surface": input_surface,
        "overlay_filename": overlay_filename,
        "output_name": output_name,
        "normalize_curvature": normalize_curvature,
        "write_diagnostics": write_diagnostics,
    }
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if coords is not None:
        params["coords"] = coords
    if average_curvature is not None:
        params["average_curvature"] = average_curvature
    if correlation_matrix is not None:
        params["correlation_matrix"] = correlation_matrix
    if scale_factor is not None:
        params["scale_factor"] = scale_factor
    if verbose_vertex is not None:
        params["verbose_vertex"] = verbose_vertex
    return params


def mrisp_write_cargs(
    params: MrispWriteParameters,
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
    cargs.append("mrisp_write")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("overlay_filename")))
    cargs.append(params.get("output_name"))
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "-SDIR",
            params.get("subjects_dir")
        ])
    if params.get("coords") is not None:
        cargs.extend([
            "-coords",
            params.get("coords")
        ])
    if params.get("average_curvature") is not None:
        cargs.extend([
            "-A",
            str(params.get("average_curvature"))
        ])
    if params.get("correlation_matrix") is not None:
        cargs.extend([
            "-CORR",
            execution.input_file(params.get("correlation_matrix"))
        ])
    if params.get("scale_factor") is not None:
        cargs.extend([
            "-SCALE",
            str(params.get("scale_factor"))
        ])
    if params.get("normalize_curvature"):
        cargs.append("-N")
    if params.get("verbose_vertex") is not None:
        cargs.extend([
            "-V",
            str(params.get("verbose_vertex"))
        ])
    if params.get("write_diagnostics"):
        cargs.append("-W")
    return cargs


def mrisp_write_outputs(
    params: MrispWriteParameters,
    execution: Execution,
) -> MrispWriteOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrispWriteOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_name")),
    )
    return ret


def mrisp_write_execute(
    params: MrispWriteParameters,
    execution: Execution,
) -> MrispWriteOutputs:
    """
    This tool converts a surface overlay on a sphere into spherical coordinates.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrispWriteOutputs`).
    """
    params = execution.params(params)
    cargs = mrisp_write_cargs(params, execution)
    ret = mrisp_write_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrisp_write(
    input_surface: InputPathType,
    overlay_filename: InputPathType,
    output_name: str,
    subjects_dir: str | None = None,
    coords: str | None = None,
    average_curvature: float | None = None,
    correlation_matrix: InputPathType | None = None,
    scale_factor: float | None = None,
    normalize_curvature: bool = False,
    verbose_vertex: float | None = None,
    write_diagnostics: bool = False,
    runner: Runner | None = None,
) -> MrispWriteOutputs:
    """
    This tool converts a surface overlay on a sphere into spherical coordinates.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Full path to input surface.
        overlay_filename: Full path to the overlay to map.
        output_name: Output file name. Can be full path to a .tif or .mgz file.
        subjects_dir: Set SUBJECTS_DIR. Default: uses environment variable.
        coords: Treat overlay as a surface and write it into a 3 frame\
            parameterization.
        average_curvature: Average curvature patterns navgs times.
        correlation_matrix: Use the overlay to compute the correlation matrix\
            within the specified label.
        scale_factor: Scale factor to adjust resolution of the spherical map.
        normalize_curvature: Normalize curvature by variance.
        verbose_vertex: Invoke diagnostics for specified vertex number.
        write_diagnostics: Write some diagnostics.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrispWriteOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRISP_WRITE_METADATA)
    params = mrisp_write_params(
        input_surface=input_surface,
        overlay_filename=overlay_filename,
        output_name=output_name,
        subjects_dir=subjects_dir,
        coords=coords,
        average_curvature=average_curvature,
        correlation_matrix=correlation_matrix,
        scale_factor=scale_factor,
        normalize_curvature=normalize_curvature,
        verbose_vertex=verbose_vertex,
        write_diagnostics=write_diagnostics,
    )
    return mrisp_write_execute(params, execution)


__all__ = [
    "MRISP_WRITE_METADATA",
    "MrispWriteOutputs",
    "MrispWriteParameters",
    "mrisp_write",
    "mrisp_write_params",
]
