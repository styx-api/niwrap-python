# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_EMPTY_METADATA = Metadata(
    id="d95bc850048040b099fd6ef056090b564f3ff824.boutiques",
    name="3dEmpty",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dEmptyParameters = typing.TypedDict('V3dEmptyParameters', {
    "__STYX_TYPE__": typing.Literal["3dEmpty"],
    "prefix": typing.NotRequired[str | None],
    "geometry": typing.NotRequired[str | None],
    "nxyz": typing.NotRequired[list[float] | None],
    "nt": typing.NotRequired[float | None],
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
        "3dEmpty": v_3d_empty_cargs,
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
        "3dEmpty": v_3d_empty_outputs,
    }.get(t)


class V3dEmptyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_empty(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Output empty dataset header file"""


def v_3d_empty_params(
    prefix: str | None = None,
    geometry: str | None = None,
    nxyz: list[float] | None = None,
    nt_: float | None = None,
) -> V3dEmptyParameters:
    """
    Build parameters.
    
    Args:
        prefix: Prefix name for output file (default = 'Empty').
        geometry: Set the 3D geometry of the grid using a string of the form\
            'MATRIX(a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34):nx,ny,nz'.
        nxyz: Set number of voxels to 'x', 'y', and 'z' along the 3 axes\
            [defaults=64].
        nt_: Number of time points [default=1].
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dEmpty",
    }
    if prefix is not None:
        params["prefix"] = prefix
    if geometry is not None:
        params["geometry"] = geometry
    if nxyz is not None:
        params["nxyz"] = nxyz
    if nt_ is not None:
        params["nt"] = nt_
    return params


def v_3d_empty_cargs(
    params: V3dEmptyParameters,
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
    cargs.append("3dEmpty")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("geometry") is not None:
        cargs.extend([
            "-geometry",
            params.get("geometry")
        ])
    if params.get("nxyz") is not None:
        cargs.extend([
            "-nxyz",
            *map(str, params.get("nxyz"))
        ])
    if params.get("nt") is not None:
        cargs.extend([
            "-nt",
            str(params.get("nt"))
        ])
    return cargs


def v_3d_empty_outputs(
    params: V3dEmptyParameters,
    execution: Execution,
) -> V3dEmptyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dEmptyOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("prefix") + ".HEAD") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_empty_execute(
    params: V3dEmptyParameters,
    execution: Execution,
) -> V3dEmptyOutputs:
    """
    Tool to create an 'empty' dataset .HEAD file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dEmptyOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_empty_cargs(params, execution)
    ret = v_3d_empty_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_empty(
    prefix: str | None = None,
    geometry: str | None = None,
    nxyz: list[float] | None = None,
    nt_: float | None = None,
    runner: Runner | None = None,
) -> V3dEmptyOutputs:
    """
    Tool to create an 'empty' dataset .HEAD file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix name for output file (default = 'Empty').
        geometry: Set the 3D geometry of the grid using a string of the form\
            'MATRIX(a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34):nx,ny,nz'.
        nxyz: Set number of voxels to 'x', 'y', and 'z' along the 3 axes\
            [defaults=64].
        nt_: Number of time points [default=1].
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dEmptyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_EMPTY_METADATA)
    params = v_3d_empty_params(
        prefix=prefix,
        geometry=geometry,
        nxyz=nxyz,
        nt_=nt_,
    )
    return v_3d_empty_execute(params, execution)


__all__ = [
    "V3dEmptyOutputs",
    "V3dEmptyParameters",
    "V_3D_EMPTY_METADATA",
    "v_3d_empty",
    "v_3d_empty_params",
]
