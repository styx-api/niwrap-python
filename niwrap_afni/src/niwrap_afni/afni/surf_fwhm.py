# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_FWHM_METADATA = Metadata(
    id="5f3d67852b7237a8609f944b36387016b6ab2c24.boutiques",
    name="SurfFWHM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


SurfFwhmParameters = typing.TypedDict('SurfFwhmParameters', {
    "__STYX_TYPE__": typing.Literal["SurfFWHM"],
    "input_file": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "surf_1": typing.NotRequired[str | None],
    "surf_sphere": typing.NotRequired[str | None],
    "clean": bool,
    "detrend": typing.NotRequired[float | None],
    "detpoly": typing.NotRequired[float | None],
    "detprefix": typing.NotRequired[str | None],
    "prefix": typing.NotRequired[str | None],
    "vox_size": typing.NotRequired[float | None],
    "neighborhood": typing.NotRequired[float | None],
    "ok_warn": bool,
    "examples": bool,
    "slice": bool,
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
        "SurfFWHM": surf_fwhm_cargs,
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
        "SurfFWHM": surf_fwhm_outputs,
    }.get(t)


class SurfFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    detrended_output: OutputPathType | None
    """Detrended dataset."""
    main_output: OutputPathType | None
    """Main output dataset."""
    histogram_output: OutputPathType | None
    """Histogram showing the distribution of local FWHM."""
    mask_output: OutputPathType | None
    """Mask output dataset."""


def surf_fwhm_params(
    input_file: InputPathType,
    mask: InputPathType | None = None,
    surf_1: str | None = None,
    surf_sphere: str | None = None,
    clean: bool = False,
    detrend: float | None = None,
    detpoly: float | None = None,
    detprefix: str | None = None,
    prefix: str | None = None,
    vox_size: float | None = None,
    neighborhood: float | None = None,
    ok_warn: bool = False,
    examples: bool = False,
    slice_: bool = False,
) -> SurfFwhmParameters:
    """
    Build parameters.
    
    Args:
        input_file: Dataset for which the FWHM is to be calculated.
        mask: Node mask so that only nodes in the mask are used to obtain\
            estimates.
        surf_1: Option for specifying the surface over which the input dataset\
            is defined.
        surf_sphere: Spherical version of -SURF_1 for Local FWHM estimates.
        clean: Strip text from output to simplify parsing.
        detrend: Detrend to order 'q'. If q is not given, the program picks\
            q=NT/30.
        detpoly: Detrend with polynomials of order p.
        detprefix: Save the detrended file into a dataset with prefix 'd'.
        prefix: Prefix of output data set.
        vox_size: Specify the nominal voxel size in mm.
        neighborhood: Neighborhood radius R for local FWHM estimates.
        ok_warn: Flag to set the mode to ok_warn.
        examples: Show command line examples and quit.
        slice_: Use the contours from planar intersections to estimate\
            gradients. For testing and development purposes only.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfFWHM",
        "input_file": input_file,
        "clean": clean,
        "ok_warn": ok_warn,
        "examples": examples,
        "slice": slice_,
    }
    if mask is not None:
        params["mask"] = mask
    if surf_1 is not None:
        params["surf_1"] = surf_1
    if surf_sphere is not None:
        params["surf_sphere"] = surf_sphere
    if detrend is not None:
        params["detrend"] = detrend
    if detpoly is not None:
        params["detpoly"] = detpoly
    if detprefix is not None:
        params["detprefix"] = detprefix
    if prefix is not None:
        params["prefix"] = prefix
    if vox_size is not None:
        params["vox_size"] = vox_size
    if neighborhood is not None:
        params["neighborhood"] = neighborhood
    return params


def surf_fwhm_cargs(
    params: SurfFwhmParameters,
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
    cargs.append("SurfFWHM")
    cargs.append(execution.input_file(params.get("input_file")))
    if params.get("mask") is not None:
        cargs.extend([
            "-MASK",
            execution.input_file(params.get("mask"))
        ])
    if params.get("surf_1") is not None:
        cargs.extend([
            "-SURF_1",
            params.get("surf_1")
        ])
    if params.get("surf_sphere") is not None:
        cargs.extend([
            "-SURF_SPHERE",
            params.get("surf_sphere")
        ])
    if params.get("clean"):
        cargs.append("-clean")
    if params.get("detrend") is not None:
        cargs.extend([
            "-detrend",
            str(params.get("detrend"))
        ])
    if params.get("detpoly") is not None:
        cargs.extend([
            "-detpoly",
            str(params.get("detpoly"))
        ])
    if params.get("detprefix") is not None:
        cargs.extend([
            "-detprefix",
            params.get("detprefix")
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("vox_size") is not None:
        cargs.extend([
            "-vox_size",
            str(params.get("vox_size"))
        ])
    if params.get("neighborhood") is not None:
        cargs.extend([
            "-hood",
            str(params.get("neighborhood"))
        ])
    if params.get("ok_warn"):
        cargs.append("-ok_warn")
    if params.get("examples"):
        cargs.append("-examples")
    if params.get("slice"):
        cargs.append("-slice")
    return cargs


def surf_fwhm_outputs(
    params: SurfFwhmParameters,
    execution: Execution,
) -> SurfFwhmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfFwhmOutputs(
        root=execution.output_file("."),
        detrended_output=execution.output_file(params.get("prefix") + ".1D.dset") if (params.get("prefix") is not None) else None,
        main_output=execution.output_file(params.get("prefix") + ".nii.gz") if (params.get("prefix") is not None) else None,
        histogram_output=execution.output_file(params.get("prefix") + "_histog.1D") if (params.get("prefix") is not None) else None,
        mask_output=execution.output_file(params.get("prefix") + "_mask.nii.gz") if (params.get("prefix") is not None) else None,
    )
    return ret


def surf_fwhm_execute(
    params: SurfFwhmParameters,
    execution: Execution,
) -> SurfFwhmOutputs:
    """
    A program for calculating local and global FWHM.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfFwhmOutputs`).
    """
    params = execution.params(params)
    cargs = surf_fwhm_cargs(params, execution)
    ret = surf_fwhm_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_fwhm(
    input_file: InputPathType,
    mask: InputPathType | None = None,
    surf_1: str | None = None,
    surf_sphere: str | None = None,
    clean: bool = False,
    detrend: float | None = None,
    detpoly: float | None = None,
    detprefix: str | None = None,
    prefix: str | None = None,
    vox_size: float | None = None,
    neighborhood: float | None = None,
    ok_warn: bool = False,
    examples: bool = False,
    slice_: bool = False,
    runner: Runner | None = None,
) -> SurfFwhmOutputs:
    """
    A program for calculating local and global FWHM.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Dataset for which the FWHM is to be calculated.
        mask: Node mask so that only nodes in the mask are used to obtain\
            estimates.
        surf_1: Option for specifying the surface over which the input dataset\
            is defined.
        surf_sphere: Spherical version of -SURF_1 for Local FWHM estimates.
        clean: Strip text from output to simplify parsing.
        detrend: Detrend to order 'q'. If q is not given, the program picks\
            q=NT/30.
        detpoly: Detrend with polynomials of order p.
        detprefix: Save the detrended file into a dataset with prefix 'd'.
        prefix: Prefix of output data set.
        vox_size: Specify the nominal voxel size in mm.
        neighborhood: Neighborhood radius R for local FWHM estimates.
        ok_warn: Flag to set the mode to ok_warn.
        examples: Show command line examples and quit.
        slice_: Use the contours from planar intersections to estimate\
            gradients. For testing and development purposes only.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfFwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_FWHM_METADATA)
    params = surf_fwhm_params(
        input_file=input_file,
        mask=mask,
        surf_1=surf_1,
        surf_sphere=surf_sphere,
        clean=clean,
        detrend=detrend,
        detpoly=detpoly,
        detprefix=detprefix,
        prefix=prefix,
        vox_size=vox_size,
        neighborhood=neighborhood,
        ok_warn=ok_warn,
        examples=examples,
        slice_=slice_,
    )
    return surf_fwhm_execute(params, execution)


__all__ = [
    "SURF_FWHM_METADATA",
    "SurfFwhmOutputs",
    "SurfFwhmParameters",
    "surf_fwhm",
    "surf_fwhm_params",
]
