# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DEDGEDOG_METADATA = Metadata(
    id="d8ea0ba3919d19e8494c7f6b252c74f682d34b17.boutiques",
    name="3dedgedog",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dedgedogParameters = typing.TypedDict('V3dedgedogParameters', {
    "__STYXTYPE__": typing.Literal["3dedgedog"],
    "input": InputPathType,
    "prefix": str,
    "mask": typing.NotRequired[InputPathType | None],
    "automask": typing.NotRequired[str | None],
    "sigma_rad": typing.NotRequired[float | None],
    "sigma_nvox": typing.NotRequired[float | None],
    "ratio_sigma": typing.NotRequired[float | None],
    "output_intermed": bool,
    "edge_bnd_nn": typing.NotRequired[float | None],
    "edge_bnd_side": typing.NotRequired[str | None],
    "edge_bnd_scale": bool,
    "only2d": typing.NotRequired[str | None],
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
        "3dedgedog": v_3dedgedog_cargs,
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
        "3dedgedog": v_3dedgedog_outputs,
    }.get(t)


class V3dedgedogOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dedgedog(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_edge: OutputPathType
    """Output edge dataset"""
    out_dog: OutputPathType
    """Output difference of Gaussian dataset"""
    out_edt2: OutputPathType
    """Output Euclidean Distance Transform squared dataset"""
    out_blur_inner: OutputPathType
    """Output inner Gaussian blurred dataset"""
    out_blur_outer: OutputPathType
    """Output outer Gaussian blurred dataset"""


def v_3dedgedog_params(
    input_: InputPathType,
    prefix: str,
    mask: InputPathType | None = None,
    automask: str | None = None,
    sigma_rad: float | None = None,
    sigma_nvox: float | None = None,
    ratio_sigma: float | None = None,
    output_intermed: bool = False,
    edge_bnd_nn: float | None = None,
    edge_bnd_side: str | None = None,
    edge_bnd_scale: bool = False,
    only2d: str | None = None,
) -> V3dedgedogParameters:
    """
    Build parameters.
    
    Args:
        input_: Input dataset.
        prefix: Output prefix name.
        mask: Mask dataset applied after Euclidean Distance Transform\
            calculation.
        automask: Calculate mask automatically. Optionally, you can provide an\
            integer X to dilate the initial automask X times (e.g., -automask+X).
        sigma_rad: Radius for 'inner' Gaussian, in mm; must be greater than 0\
            (default: 1.40).
        sigma_nvox: Define radius for 'inner' Gaussian by providing a\
            multiplicative factor for voxel edge length greater than 0 (default:\
            use sigma_rad).
        ratio_sigma: Ratio of inner and outer Gaussian sigma values (default:\
            1.40).
        output_intermed: Output intermediate datasets: DOG, EDT2, BLURS\
            (default: not output).
        edge_bnd_nn: Nearest neighbor (NN) value for connectedness of\
            boundaries; must be 1 (face only), 2 (face+edge), or 3 (face+edge+node)\
            (default: 1).
        edge_bnd_side: Specify boundary layer to use: NEG, POS, BOTH, BOTH_SIGN\
            (default: NEG).
        edge_bnd_scale: Scale edge values to have relative magnitude between 0\
            and 100 (default: edge locations have value=1).
        only2d: Calculate edges in 2D per plane specified by SLI: 'axi', 'cor',\
            'sag'.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dedgedog",
        "input": input_,
        "prefix": prefix,
        "output_intermed": output_intermed,
        "edge_bnd_scale": edge_bnd_scale,
    }
    if mask is not None:
        params["mask"] = mask
    if automask is not None:
        params["automask"] = automask
    if sigma_rad is not None:
        params["sigma_rad"] = sigma_rad
    if sigma_nvox is not None:
        params["sigma_nvox"] = sigma_nvox
    if ratio_sigma is not None:
        params["ratio_sigma"] = ratio_sigma
    if edge_bnd_nn is not None:
        params["edge_bnd_nn"] = edge_bnd_nn
    if edge_bnd_side is not None:
        params["edge_bnd_side"] = edge_bnd_side
    if only2d is not None:
        params["only2d"] = only2d
    return params


def v_3dedgedog_cargs(
    params: V3dedgedogParameters,
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
    cargs.append("3dedgedog")
    cargs.append(execution.input_file(params.get("input")))
    cargs.append(params.get("prefix"))
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("automask") is not None:
        cargs.extend([
            "-automask",
            params.get("automask")
        ])
    if params.get("sigma_rad") is not None:
        cargs.extend([
            "-sigma_rad",
            str(params.get("sigma_rad"))
        ])
    if params.get("sigma_nvox") is not None:
        cargs.extend([
            "-sigma_nvox",
            str(params.get("sigma_nvox"))
        ])
    if params.get("ratio_sigma") is not None:
        cargs.extend([
            "-ratio_sigma",
            str(params.get("ratio_sigma"))
        ])
    if params.get("output_intermed"):
        cargs.append("-output_intermed")
    if params.get("edge_bnd_nn") is not None:
        cargs.extend([
            "-edge_bnd_NN",
            str(params.get("edge_bnd_nn"))
        ])
    if params.get("edge_bnd_side") is not None:
        cargs.extend([
            "-edge_bnd_side",
            params.get("edge_bnd_side")
        ])
    if params.get("edge_bnd_scale"):
        cargs.append("-edge_bnd_scale")
    if params.get("only2d") is not None:
        cargs.extend([
            "-only2D",
            params.get("only2d")
        ])
    return cargs


def v_3dedgedog_outputs(
    params: V3dedgedogParameters,
    execution: Execution,
) -> V3dedgedogOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dedgedogOutputs(
        root=execution.output_file("."),
        out_edge=execution.output_file(params.get("prefix") + "_edge.nii.gz"),
        out_dog=execution.output_file(params.get("prefix") + "_dog.nii.gz"),
        out_edt2=execution.output_file(params.get("prefix") + "_edt2.nii.gz"),
        out_blur_inner=execution.output_file(params.get("prefix") + "_blur_inner.nii.gz"),
        out_blur_outer=execution.output_file(params.get("prefix") + "_blur_outer.nii.gz"),
    )
    return ret


def v_3dedgedog_execute(
    params: V3dedgedogParameters,
    execution: Execution,
) -> V3dedgedogOutputs:
    """
    Calculate edges in an image using the Difference of Gaussians (DOG) method with
    extensions/tweaks of the Marr-Hildreth algorithm.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dedgedogOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dedgedog_cargs(params, execution)
    ret = v_3dedgedog_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dedgedog(
    input_: InputPathType,
    prefix: str,
    mask: InputPathType | None = None,
    automask: str | None = None,
    sigma_rad: float | None = None,
    sigma_nvox: float | None = None,
    ratio_sigma: float | None = None,
    output_intermed: bool = False,
    edge_bnd_nn: float | None = None,
    edge_bnd_side: str | None = None,
    edge_bnd_scale: bool = False,
    only2d: str | None = None,
    runner: Runner | None = None,
) -> V3dedgedogOutputs:
    """
    Calculate edges in an image using the Difference of Gaussians (DOG) method with
    extensions/tweaks of the Marr-Hildreth algorithm.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_: Input dataset.
        prefix: Output prefix name.
        mask: Mask dataset applied after Euclidean Distance Transform\
            calculation.
        automask: Calculate mask automatically. Optionally, you can provide an\
            integer X to dilate the initial automask X times (e.g., -automask+X).
        sigma_rad: Radius for 'inner' Gaussian, in mm; must be greater than 0\
            (default: 1.40).
        sigma_nvox: Define radius for 'inner' Gaussian by providing a\
            multiplicative factor for voxel edge length greater than 0 (default:\
            use sigma_rad).
        ratio_sigma: Ratio of inner and outer Gaussian sigma values (default:\
            1.40).
        output_intermed: Output intermediate datasets: DOG, EDT2, BLURS\
            (default: not output).
        edge_bnd_nn: Nearest neighbor (NN) value for connectedness of\
            boundaries; must be 1 (face only), 2 (face+edge), or 3 (face+edge+node)\
            (default: 1).
        edge_bnd_side: Specify boundary layer to use: NEG, POS, BOTH, BOTH_SIGN\
            (default: NEG).
        edge_bnd_scale: Scale edge values to have relative magnitude between 0\
            and 100 (default: edge locations have value=1).
        only2d: Calculate edges in 2D per plane specified by SLI: 'axi', 'cor',\
            'sag'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dedgedogOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DEDGEDOG_METADATA)
    params = v_3dedgedog_params(
        input_=input_,
        prefix=prefix,
        mask=mask,
        automask=automask,
        sigma_rad=sigma_rad,
        sigma_nvox=sigma_nvox,
        ratio_sigma=ratio_sigma,
        output_intermed=output_intermed,
        edge_bnd_nn=edge_bnd_nn,
        edge_bnd_side=edge_bnd_side,
        edge_bnd_scale=edge_bnd_scale,
        only2d=only2d,
    )
    return v_3dedgedog_execute(params, execution)


__all__ = [
    "V3dedgedogOutputs",
    "V3dedgedogParameters",
    "V_3DEDGEDOG_METADATA",
    "v_3dedgedog",
    "v_3dedgedog_params",
]
