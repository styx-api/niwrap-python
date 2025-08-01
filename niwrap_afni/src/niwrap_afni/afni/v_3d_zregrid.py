# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ZREGRID_METADATA = Metadata(
    id="db022b59eef3bb41c838694c65e5ebc0749928b2.boutiques",
    name="3dZregrid",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dZregridParameters = typing.TypedDict('V3dZregridParameters', {
    "__STYXTYPE__": typing.Literal["3dZregrid"],
    "z_thickness": typing.NotRequired[float | None],
    "slice_count": typing.NotRequired[float | None],
    "z_size": typing.NotRequired[float | None],
    "prefix": typing.NotRequired[str | None],
    "infile": InputPathType,
    "verbose": bool,
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
        "3dZregrid": v_3d_zregrid_cargs,
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
        "3dZregrid": v_3d_zregrid_outputs,
    }.get(t)


class V3dZregridOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_zregrid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_head: OutputPathType | None
    """Output dataset with new grid"""
    outfile_brik: OutputPathType | None
    """Output dataset with new grid"""


def v_3d_zregrid_params(
    infile: InputPathType,
    z_thickness: float | None = None,
    slice_count: float | None = None,
    z_size: float | None = None,
    prefix: str | None = None,
    verbose: bool = False,
) -> V3dZregridParameters:
    """
    Build parameters.
    
    Args:
        infile: Input dataset.
        z_thickness: Set slice thickness to D mm.
        slice_count: Set slice count to N.
        z_size: Set thickness of dataset (center-to-center of first and last\
            slices) to Z mm.
        prefix: Write result to dataset with prefix P.
        verbose: Write progress reports to stderr.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dZregrid",
        "infile": infile,
        "verbose": verbose,
    }
    if z_thickness is not None:
        params["z_thickness"] = z_thickness
    if slice_count is not None:
        params["slice_count"] = slice_count
    if z_size is not None:
        params["z_size"] = z_size
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_zregrid_cargs(
    params: V3dZregridParameters,
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
    cargs.append("3dZregrid")
    if params.get("z_thickness") is not None:
        cargs.extend([
            "-dz",
            str(params.get("z_thickness"))
        ])
    if params.get("slice_count") is not None:
        cargs.extend([
            "-nz",
            str(params.get("slice_count"))
        ])
    if params.get("z_size") is not None:
        cargs.extend([
            "-zsize",
            str(params.get("z_size"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    cargs.append(execution.input_file(params.get("infile")))
    if params.get("verbose"):
        cargs.append("-verb")
    return cargs


def v_3d_zregrid_outputs(
    params: V3dZregridParameters,
    execution: Execution,
) -> V3dZregridOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dZregridOutputs(
        root=execution.output_file("."),
        outfile_head=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
        outfile_brik=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_zregrid_execute(
    params: V3dZregridParameters,
    execution: Execution,
) -> V3dZregridOutputs:
    """
    Alters the input dataset's slice thickness and/or number.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dZregridOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_zregrid_cargs(params, execution)
    ret = v_3d_zregrid_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_zregrid(
    infile: InputPathType,
    z_thickness: float | None = None,
    slice_count: float | None = None,
    z_size: float | None = None,
    prefix: str | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> V3dZregridOutputs:
    """
    Alters the input dataset's slice thickness and/or number.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input dataset.
        z_thickness: Set slice thickness to D mm.
        slice_count: Set slice count to N.
        z_size: Set thickness of dataset (center-to-center of first and last\
            slices) to Z mm.
        prefix: Write result to dataset with prefix P.
        verbose: Write progress reports to stderr.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dZregridOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ZREGRID_METADATA)
    params = v_3d_zregrid_params(
        z_thickness=z_thickness,
        slice_count=slice_count,
        z_size=z_size,
        prefix=prefix,
        infile=infile,
        verbose=verbose,
    )
    return v_3d_zregrid_execute(params, execution)


__all__ = [
    "V3dZregridOutputs",
    "V3dZregridParameters",
    "V_3D_ZREGRID_METADATA",
    "v_3d_zregrid",
    "v_3d_zregrid_params",
]
