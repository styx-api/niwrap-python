# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_MODIFY_SPHERE_METADATA = Metadata(
    id="7ba7bdfa9f75a3f280b0446651d5074e673b22aa.boutiques",
    name="surface-modify-sphere",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


SurfaceModifySphereParameters = typing.TypedDict('SurfaceModifySphereParameters', {
    "__STYX_TYPE__": typing.Literal["surface-modify-sphere"],
    "sphere_in": InputPathType,
    "radius": float,
    "sphere_out": str,
    "opt_recenter": bool,
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
        "surface-modify-sphere": surface_modify_sphere_cargs,
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
        "surface-modify-sphere": surface_modify_sphere_outputs,
    }.get(t)


class SurfaceModifySphereOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_modify_sphere(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sphere_out: OutputPathType
    """the output sphere"""


def surface_modify_sphere_params(
    sphere_in: InputPathType,
    radius: float,
    sphere_out: str,
    opt_recenter: bool = False,
) -> SurfaceModifySphereParameters:
    """
    Build parameters.
    
    Args:
        sphere_in: the sphere to modify.
        radius: the radius the output sphere should have.
        sphere_out: the output sphere.
        opt_recenter: recenter the sphere by means of the bounding box.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-modify-sphere",
        "sphere_in": sphere_in,
        "radius": radius,
        "sphere_out": sphere_out,
        "opt_recenter": opt_recenter,
    }
    return params


def surface_modify_sphere_cargs(
    params: SurfaceModifySphereParameters,
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
    cargs.append("-surface-modify-sphere")
    cargs.append(execution.input_file(params.get("sphere_in")))
    cargs.append(str(params.get("radius")))
    cargs.append(params.get("sphere_out"))
    if params.get("opt_recenter"):
        cargs.append("-recenter")
    return cargs


def surface_modify_sphere_outputs(
    params: SurfaceModifySphereParameters,
    execution: Execution,
) -> SurfaceModifySphereOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceModifySphereOutputs(
        root=execution.output_file("."),
        sphere_out=execution.output_file(params.get("sphere_out")),
    )
    return ret


def surface_modify_sphere_execute(
    params: SurfaceModifySphereParameters,
    execution: Execution,
) -> SurfaceModifySphereOutputs:
    """
    Change radius and optionally recenter a sphere.
    
    This command may be useful if you have used -surface-resample to resample a
    sphere, which can suffer from problems generally not present in
    -surface-sphere-project-unproject. If the sphere should already be centered
    around the origin, using -recenter may still shift it slightly before
    changing the radius, which is likely to be undesireable.
    
    If <sphere-in> is not close to spherical, or not centered around the origin
    and -recenter is not used, a warning is printed.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceModifySphereOutputs`).
    """
    params = execution.params(params)
    cargs = surface_modify_sphere_cargs(params, execution)
    ret = surface_modify_sphere_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_modify_sphere(
    sphere_in: InputPathType,
    radius: float,
    sphere_out: str,
    opt_recenter: bool = False,
    runner: Runner | None = None,
) -> SurfaceModifySphereOutputs:
    """
    Change radius and optionally recenter a sphere.
    
    This command may be useful if you have used -surface-resample to resample a
    sphere, which can suffer from problems generally not present in
    -surface-sphere-project-unproject. If the sphere should already be centered
    around the origin, using -recenter may still shift it slightly before
    changing the radius, which is likely to be undesireable.
    
    If <sphere-in> is not close to spherical, or not centered around the origin
    and -recenter is not used, a warning is printed.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        sphere_in: the sphere to modify.
        radius: the radius the output sphere should have.
        sphere_out: the output sphere.
        opt_recenter: recenter the sphere by means of the bounding box.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceModifySphereOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_MODIFY_SPHERE_METADATA)
    params = surface_modify_sphere_params(
        sphere_in=sphere_in,
        radius=radius,
        sphere_out=sphere_out,
        opt_recenter=opt_recenter,
    )
    return surface_modify_sphere_execute(params, execution)


__all__ = [
    "SURFACE_MODIFY_SPHERE_METADATA",
    "SurfaceModifySphereOutputs",
    "SurfaceModifySphereParameters",
    "surface_modify_sphere",
    "surface_modify_sphere_params",
]
