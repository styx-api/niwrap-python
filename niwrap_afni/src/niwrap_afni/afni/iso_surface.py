# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ISO_SURFACE_METADATA = Metadata(
    id="ae4f55d6aa3df9abb44d283d9623f609eefee601.boutiques",
    name="IsoSurface",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


IsoSurfaceParameters = typing.TypedDict('IsoSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["IsoSurface"],
    "input_vol": typing.NotRequired[InputPathType | None],
    "shape_spec": typing.NotRequired[list[str] | None],
    "isorois": bool,
    "isoval": typing.NotRequired[str | None],
    "isorange": typing.NotRequired[list[str] | None],
    "isocmask": typing.NotRequired[str | None],
    "output_prefix": typing.NotRequired[str | None],
    "tsmooth": typing.NotRequired[list[str] | None],
    "debug": typing.NotRequired[str | None],
    "autocrop": bool,
    "remesh": typing.NotRequired[str | None],
    "xform": typing.NotRequired[str | None],
    "novolreg": bool,
    "noxform": bool,
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
        "IsoSurface": iso_surface_cargs,
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
        "IsoSurface": iso_surface_outputs,
    }.get(t)


class IsoSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `iso_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_ply: OutputPathType
    """Output isosurface in PLY format."""
    output_surface_gii: OutputPathType
    """Output isosurface in GIFTI format."""
    output_surface_stl: OutputPathType
    """Output isosurface in STL format."""


def iso_surface_params(
    input_vol: InputPathType | None = None,
    shape_spec: list[str] | None = None,
    isorois: bool = False,
    isoval: str | None = None,
    isorange: list[str] | None = None,
    isocmask: str | None = None,
    output_prefix: str | None = None,
    tsmooth: list[str] | None = None,
    debug: str | None = None,
    autocrop: bool = False,
    remesh: str | None = None,
    xform: str | None = None,
    novolreg: bool = False,
    noxform: bool = False,
) -> IsoSurfaceParameters:
    """
    Build parameters.
    
    Args:
        input_vol: Input volume file.
        shape_spec: Built-in shape specification.
        isorois: Create isosurface for each unique value in the input volume.
        isoval: Create isosurface where volume = V.
        isorange: Create isosurface where V0 <= volume < V1.
        isocmask: Create isosurface where MASK_COM != 0.
        output_prefix: Prefix of output surface file.
        tsmooth: Smooth resultant surface using Taubin smoothing with\
            parameters KPB and NITER.
        debug: Debug levels of 0 (default), 1, 2, 3.
        autocrop: Crop input volume before extraction.
        remesh: Remesh the surface(s).
        xform: Transform to apply to volume values before extracting.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations.
        noxform: Same as -novolreg.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "IsoSurface",
        "isorois": isorois,
        "autocrop": autocrop,
        "novolreg": novolreg,
        "noxform": noxform,
    }
    if input_vol is not None:
        params["input_vol"] = input_vol
    if shape_spec is not None:
        params["shape_spec"] = shape_spec
    if isoval is not None:
        params["isoval"] = isoval
    if isorange is not None:
        params["isorange"] = isorange
    if isocmask is not None:
        params["isocmask"] = isocmask
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if tsmooth is not None:
        params["tsmooth"] = tsmooth
    if debug is not None:
        params["debug"] = debug
    if remesh is not None:
        params["remesh"] = remesh
    if xform is not None:
        params["xform"] = xform
    return params


def iso_surface_cargs(
    params: IsoSurfaceParameters,
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
    cargs.append("IsoSurface")
    if params.get("input_vol") is not None:
        cargs.extend([
            "-input",
            execution.input_file(params.get("input_vol"))
        ])
    if params.get("shape_spec") is not None:
        cargs.extend([
            "-shape",
            *params.get("shape_spec")
        ])
    if params.get("isorois"):
        cargs.append("-isorois")
    if params.get("isoval") is not None:
        cargs.extend([
            "-isoval",
            params.get("isoval")
        ])
    if params.get("isorange") is not None:
        cargs.extend([
            "-isorange",
            *params.get("isorange")
        ])
    if params.get("isocmask") is not None:
        cargs.extend([
            "-isocmask",
            params.get("isocmask")
        ])
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-o_TYPE",
            params.get("output_prefix")
        ])
    if params.get("tsmooth") is not None:
        cargs.extend([
            "-Tsmooth",
            *params.get("tsmooth")
        ])
    if params.get("debug") is not None:
        cargs.extend([
            "-debug",
            params.get("debug")
        ])
    if params.get("autocrop"):
        cargs.append("-autocrop")
    if params.get("remesh") is not None:
        cargs.extend([
            "-remesh",
            params.get("remesh")
        ])
    if params.get("xform") is not None:
        cargs.extend([
            "-xform",
            params.get("xform")
        ])
    if params.get("novolreg"):
        cargs.append("-novolreg")
    if params.get("noxform"):
        cargs.append("-noxform")
    return cargs


def iso_surface_outputs(
    params: IsoSurfaceParameters,
    execution: Execution,
) -> IsoSurfaceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = IsoSurfaceOutputs(
        root=execution.output_file("."),
        output_surface_ply=execution.output_file("[MASK]_surf.ply"),
        output_surface_gii=execution.output_file("[MASK]_surf.gii"),
        output_surface_stl=execution.output_file("[MASK]_surf.stl"),
    )
    return ret


def iso_surface_execute(
    params: IsoSurfaceParameters,
    execution: Execution,
) -> IsoSurfaceOutputs:
    """
    A program to perform isosurface extraction from a volume.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `IsoSurfaceOutputs`).
    """
    params = execution.params(params)
    cargs = iso_surface_cargs(params, execution)
    ret = iso_surface_outputs(params, execution)
    execution.run(cargs)
    return ret


def iso_surface(
    input_vol: InputPathType | None = None,
    shape_spec: list[str] | None = None,
    isorois: bool = False,
    isoval: str | None = None,
    isorange: list[str] | None = None,
    isocmask: str | None = None,
    output_prefix: str | None = None,
    tsmooth: list[str] | None = None,
    debug: str | None = None,
    autocrop: bool = False,
    remesh: str | None = None,
    xform: str | None = None,
    novolreg: bool = False,
    noxform: bool = False,
    runner: Runner | None = None,
) -> IsoSurfaceOutputs:
    """
    A program to perform isosurface extraction from a volume.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_vol: Input volume file.
        shape_spec: Built-in shape specification.
        isorois: Create isosurface for each unique value in the input volume.
        isoval: Create isosurface where volume = V.
        isorange: Create isosurface where V0 <= volume < V1.
        isocmask: Create isosurface where MASK_COM != 0.
        output_prefix: Prefix of output surface file.
        tsmooth: Smooth resultant surface using Taubin smoothing with\
            parameters KPB and NITER.
        debug: Debug levels of 0 (default), 1, 2, 3.
        autocrop: Crop input volume before extraction.
        remesh: Remesh the surface(s).
        xform: Transform to apply to volume values before extracting.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations.
        noxform: Same as -novolreg.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IsoSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ISO_SURFACE_METADATA)
    params = iso_surface_params(
        input_vol=input_vol,
        shape_spec=shape_spec,
        isorois=isorois,
        isoval=isoval,
        isorange=isorange,
        isocmask=isocmask,
        output_prefix=output_prefix,
        tsmooth=tsmooth,
        debug=debug,
        autocrop=autocrop,
        remesh=remesh,
        xform=xform,
        novolreg=novolreg,
        noxform=noxform,
    )
    return iso_surface_execute(params, execution)


__all__ = [
    "ISO_SURFACE_METADATA",
    "IsoSurfaceOutputs",
    "IsoSurfaceParameters",
    "iso_surface",
    "iso_surface_params",
]
