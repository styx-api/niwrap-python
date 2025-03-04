# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF2VOL_METADATA = Metadata(
    id="f4ae5ac678a739e2426d3a890649ef1fbff288ef.boutiques",
    name="surf2vol",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Surf2volParameters = typing.TypedDict('Surf2volParameters', {
    "__STYX_TYPE__": typing.Literal["surf2vol"],
    "fixed_surface": InputPathType,
    "moving_surface": InputPathType,
    "fixed_mri": InputPathType,
    "moving_mri": InputPathType,
    "output_file": typing.NotRequired[str | None],
    "output_field": typing.NotRequired[str | None],
    "output_affine": typing.NotRequired[str | None],
    "output_surf": typing.NotRequired[str | None],
    "output_surf_affine": typing.NotRequired[str | None],
    "output_mesh": typing.NotRequired[str | None],
    "spacing_x": typing.NotRequired[float | None],
    "spacing_y": typing.NotRequired[float | None],
    "spacing_z": typing.NotRequired[float | None],
    "poisson_ratio": typing.NotRequired[float | None],
    "dirty_factor": typing.NotRequired[float | None],
    "debug_output": bool,
    "cache_transform": typing.NotRequired[str | None],
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
        "surf2vol": surf2vol_cargs,
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
        "surf2vol": surf2vol_outputs,
    }.get(t)


class Surf2volOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf2vol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Default output of the deformation process."""
    output_field: OutputPathType | None
    """Field output of the deformation process."""


def surf2vol_params(
    fixed_surface: InputPathType,
    moving_surface: InputPathType,
    fixed_mri: InputPathType,
    moving_mri: InputPathType,
    output_file: str | None = "out.mgz",
    output_field: str | None = "out_field.mgz",
    output_affine: str | None = None,
    output_surf: str | None = None,
    output_surf_affine: str | None = None,
    output_mesh: str | None = None,
    spacing_x: float | None = None,
    spacing_y: float | None = None,
    spacing_z: float | None = None,
    poisson_ratio: float | None = None,
    dirty_factor: float | None = None,
    debug_output: bool = False,
    cache_transform: str | None = None,
) -> Surf2volParameters:
    """
    Build parameters.
    
    Args:
        fixed_surface: File path for the main fixed surface.
        moving_surface: File path for the main moving surface.
        fixed_mri: Fixed volume file.
        moving_mri: Moving volume file.
        output_file: Output file for the result, default is out.mgz.
        output_field: Output field file, default is out_field.mgz.
        output_affine: Path for the output affine file.
        output_surf: Root file name for output surfaces which will have indices\
            appended for each surface.
        output_surf_affine: Root file name for output surfaces with affine\
            transformations.
        output_mesh: File path for the output mesh.
        spacing_x: Specifies the x spacing for the deformation grid.
        spacing_y: Specifies the y spacing for the deformation grid.
        spacing_z: Specifies the z spacing for the deformation grid.
        poisson_ratio: Poisson ratio for material properties, default is 0.3.
        dirty_factor: Factor for dirty regions, between 0 and 1.
        debug_output: Enable debug output, writing a morph file at each\
            iteration.
        cache_transform: Path to save transformation cache for reusing in\
            subsequent runs.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surf2vol",
        "fixed_surface": fixed_surface,
        "moving_surface": moving_surface,
        "fixed_mri": fixed_mri,
        "moving_mri": moving_mri,
        "debug_output": debug_output,
    }
    if output_file is not None:
        params["output_file"] = output_file
    if output_field is not None:
        params["output_field"] = output_field
    if output_affine is not None:
        params["output_affine"] = output_affine
    if output_surf is not None:
        params["output_surf"] = output_surf
    if output_surf_affine is not None:
        params["output_surf_affine"] = output_surf_affine
    if output_mesh is not None:
        params["output_mesh"] = output_mesh
    if spacing_x is not None:
        params["spacing_x"] = spacing_x
    if spacing_y is not None:
        params["spacing_y"] = spacing_y
    if spacing_z is not None:
        params["spacing_z"] = spacing_z
    if poisson_ratio is not None:
        params["poisson_ratio"] = poisson_ratio
    if dirty_factor is not None:
        params["dirty_factor"] = dirty_factor
    if cache_transform is not None:
        params["cache_transform"] = cache_transform
    return params


def surf2vol_cargs(
    params: Surf2volParameters,
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
    cargs.append("surf2vol")
    cargs.extend([
        "-fixed_surf",
        execution.input_file(params.get("fixed_surface"))
    ])
    cargs.extend([
        "-moving_surf",
        execution.input_file(params.get("moving_surface"))
    ])
    cargs.extend([
        "-fixed_mri",
        execution.input_file(params.get("fixed_mri"))
    ])
    cargs.extend([
        "-moving_mri",
        execution.input_file(params.get("moving_mri"))
    ])
    if params.get("output_file") is not None:
        cargs.extend([
            "-out",
            params.get("output_file")
        ])
    if params.get("output_field") is not None:
        cargs.extend([
            "-out_field",
            params.get("output_field")
        ])
    if params.get("output_affine") is not None:
        cargs.extend([
            "-out_affine",
            params.get("output_affine")
        ])
    if params.get("output_surf") is not None:
        cargs.extend([
            "-out_surf",
            params.get("output_surf")
        ])
    if params.get("output_surf_affine") is not None:
        cargs.extend([
            "-out_surf_affine",
            params.get("output_surf_affine")
        ])
    if params.get("output_mesh") is not None:
        cargs.extend([
            "-out_mesh",
            params.get("output_mesh")
        ])
    if params.get("spacing_x") is not None:
        cargs.extend([
            "-spacing_x",
            str(params.get("spacing_x"))
        ])
    if params.get("spacing_y") is not None:
        cargs.extend([
            "-spacing_y",
            str(params.get("spacing_y"))
        ])
    if params.get("spacing_z") is not None:
        cargs.extend([
            "-spacing_z",
            str(params.get("spacing_z"))
        ])
    if params.get("poisson_ratio") is not None:
        cargs.extend([
            "-poisson",
            str(params.get("poisson_ratio"))
        ])
    if params.get("dirty_factor") is not None:
        cargs.extend([
            "-dirty",
            str(params.get("dirty_factor"))
        ])
    if params.get("debug_output"):
        cargs.append("-dbg_output")
    if params.get("cache_transform") is not None:
        cargs.extend([
            "-cache_transform",
            params.get("cache_transform")
        ])
    return cargs


def surf2vol_outputs(
    params: Surf2volParameters,
    execution: Execution,
) -> Surf2volOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Surf2volOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
        output_field=execution.output_file(params.get("output_field")) if (params.get("output_field") is not None) else None,
    )
    return ret


def surf2vol_execute(
    params: Surf2volParameters,
    execution: Execution,
) -> Surf2volOutputs:
    """
    Diffuse surface deformation to volumes using surface and MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Surf2volOutputs`).
    """
    params = execution.params(params)
    cargs = surf2vol_cargs(params, execution)
    ret = surf2vol_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf2vol(
    fixed_surface: InputPathType,
    moving_surface: InputPathType,
    fixed_mri: InputPathType,
    moving_mri: InputPathType,
    output_file: str | None = "out.mgz",
    output_field: str | None = "out_field.mgz",
    output_affine: str | None = None,
    output_surf: str | None = None,
    output_surf_affine: str | None = None,
    output_mesh: str | None = None,
    spacing_x: float | None = None,
    spacing_y: float | None = None,
    spacing_z: float | None = None,
    poisson_ratio: float | None = None,
    dirty_factor: float | None = None,
    debug_output: bool = False,
    cache_transform: str | None = None,
    runner: Runner | None = None,
) -> Surf2volOutputs:
    """
    Diffuse surface deformation to volumes using surface and MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        fixed_surface: File path for the main fixed surface.
        moving_surface: File path for the main moving surface.
        fixed_mri: Fixed volume file.
        moving_mri: Moving volume file.
        output_file: Output file for the result, default is out.mgz.
        output_field: Output field file, default is out_field.mgz.
        output_affine: Path for the output affine file.
        output_surf: Root file name for output surfaces which will have indices\
            appended for each surface.
        output_surf_affine: Root file name for output surfaces with affine\
            transformations.
        output_mesh: File path for the output mesh.
        spacing_x: Specifies the x spacing for the deformation grid.
        spacing_y: Specifies the y spacing for the deformation grid.
        spacing_z: Specifies the z spacing for the deformation grid.
        poisson_ratio: Poisson ratio for material properties, default is 0.3.
        dirty_factor: Factor for dirty regions, between 0 and 1.
        debug_output: Enable debug output, writing a morph file at each\
            iteration.
        cache_transform: Path to save transformation cache for reusing in\
            subsequent runs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Surf2volOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF2VOL_METADATA)
    params = surf2vol_params(
        fixed_surface=fixed_surface,
        moving_surface=moving_surface,
        fixed_mri=fixed_mri,
        moving_mri=moving_mri,
        output_file=output_file,
        output_field=output_field,
        output_affine=output_affine,
        output_surf=output_surf,
        output_surf_affine=output_surf_affine,
        output_mesh=output_mesh,
        spacing_x=spacing_x,
        spacing_y=spacing_y,
        spacing_z=spacing_z,
        poisson_ratio=poisson_ratio,
        dirty_factor=dirty_factor,
        debug_output=debug_output,
        cache_transform=cache_transform,
    )
    return surf2vol_execute(params, execution)


__all__ = [
    "SURF2VOL_METADATA",
    "Surf2volOutputs",
    "Surf2volParameters",
    "surf2vol",
    "surf2vol_params",
]
