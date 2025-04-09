# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_MESH_METADATA = Metadata(
    id="6066359d8c294ca53c640b4ebcdab63e664ed84c.boutiques",
    name="SurfMesh",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


SurfMeshParameters = typing.TypedDict('SurfMeshParameters', {
    "__STYX_TYPE__": typing.Literal["SurfMesh"],
    "input_surface": str,
    "output_surface": str,
    "edge_fraction": float,
    "surface_volume": typing.NotRequired[InputPathType | None],
    "one_state": bool,
    "anatomical_label": bool,
    "no_volume_registration": bool,
    "set_env": typing.NotRequired[str | None],
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
        "SurfMesh": surf_mesh_cargs,
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
        "SurfMesh": surf_mesh_outputs,
    }.get(t)


class SurfMeshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_mesh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_file: OutputPathType
    """Output surface file"""


def surf_mesh_params(
    input_surface: str,
    output_surface: str,
    edge_fraction: float,
    surface_volume: InputPathType | None = None,
    one_state: bool = False,
    anatomical_label: bool = False,
    no_volume_registration: bool = False,
    set_env: str | None = None,
) -> SurfMeshParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file with specified type.
        output_surface: Output surface file with specified type.
        edge_fraction: Fraction of edges to simplify the surface.
        surface_volume: Surface volume file.
        one_state: Make all input surfaces have the same state.
        anatomical_label: Label all input surfaces as anatomically correct.
        no_volume_registration: Ignore any Rotate, Volreg, Tagalign, or\
            WarpDrive transformations present in the Surface Volume.
        set_env: Set environment variable.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfMesh",
        "input_surface": input_surface,
        "output_surface": output_surface,
        "edge_fraction": edge_fraction,
        "one_state": one_state,
        "anatomical_label": anatomical_label,
        "no_volume_registration": no_volume_registration,
    }
    if surface_volume is not None:
        params["surface_volume"] = surface_volume
    if set_env is not None:
        params["set_env"] = set_env
    return params


def surf_mesh_cargs(
    params: SurfMeshParameters,
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
    cargs.append("SurfMesh")
    cargs.extend([
        "-i_TYPE",
        params.get("input_surface")
    ])
    cargs.extend([
        "-o_TYPE",
        params.get("output_surface")
    ])
    cargs.extend([
        "-edges",
        str(params.get("edge_fraction"))
    ])
    if params.get("surface_volume") is not None:
        cargs.extend([
            "-sv",
            execution.input_file(params.get("surface_volume"))
        ])
    if params.get("one_state"):
        cargs.append("-onestate")
    if params.get("anatomical_label"):
        cargs.append("-anatomical")
    if params.get("no_volume_registration"):
        cargs.append("-novolreg")
    if params.get("set_env") is not None:
        cargs.extend([
            "-setenv",
            params.get("set_env")
        ])
    return cargs


def surf_mesh_outputs(
    params: SurfMeshParameters,
    execution: Execution,
) -> SurfMeshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfMeshOutputs(
        root=execution.output_file("."),
        output_surface_file=execution.output_file(params.get("output_surface") + ".surface"),
    )
    return ret


def surf_mesh_execute(
    params: SurfMeshParameters,
    execution: Execution,
) -> SurfMeshOutputs:
    """
    Surface mesh manipulation tool.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfMeshOutputs`).
    """
    params = execution.params(params)
    cargs = surf_mesh_cargs(params, execution)
    ret = surf_mesh_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_mesh(
    input_surface: str,
    output_surface: str,
    edge_fraction: float,
    surface_volume: InputPathType | None = None,
    one_state: bool = False,
    anatomical_label: bool = False,
    no_volume_registration: bool = False,
    set_env: str | None = None,
    runner: Runner | None = None,
) -> SurfMeshOutputs:
    """
    Surface mesh manipulation tool.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_surface: Input surface file with specified type.
        output_surface: Output surface file with specified type.
        edge_fraction: Fraction of edges to simplify the surface.
        surface_volume: Surface volume file.
        one_state: Make all input surfaces have the same state.
        anatomical_label: Label all input surfaces as anatomically correct.
        no_volume_registration: Ignore any Rotate, Volreg, Tagalign, or\
            WarpDrive transformations present in the Surface Volume.
        set_env: Set environment variable.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfMeshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_MESH_METADATA)
    params = surf_mesh_params(
        input_surface=input_surface,
        output_surface=output_surface,
        edge_fraction=edge_fraction,
        surface_volume=surface_volume,
        one_state=one_state,
        anatomical_label=anatomical_label,
        no_volume_registration=no_volume_registration,
        set_env=set_env,
    )
    return surf_mesh_execute(params, execution)


__all__ = [
    "SURF_MESH_METADATA",
    "SurfMeshOutputs",
    "SurfMeshParameters",
    "surf_mesh",
    "surf_mesh_params",
]
