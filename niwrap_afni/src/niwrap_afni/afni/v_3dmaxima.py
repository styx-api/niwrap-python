# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DMAXIMA_METADATA = Metadata(
    id="f8ba8da054bfe915efd0d6532d6b8fe26bfcc7a9.boutiques",
    name="3dmaxima",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dmaximaParameters = typing.TypedDict('V3dmaximaParameters', {
    "__STYX_TYPE__": typing.Literal["3dmaxima"],
    "input_dataset": InputPathType,
    "output_prefix": typing.NotRequired[str | None],
    "threshold": typing.NotRequired[float | None],
    "min_dist": typing.NotRequired[float | None],
    "out_rad": typing.NotRequired[float | None],
    "input_flag": bool,
    "spheres_1_flag": bool,
    "spheres_1toN_flag": bool,
    "spheres_Nto1_flag": bool,
    "neg_ext_flag": bool,
    "true_max_flag": bool,
    "dset_coords_flag": bool,
    "no_text_flag": bool,
    "coords_only_flag": bool,
    "n_style_sort_flag": bool,
    "n_style_weight_ave_flag": bool,
    "debug_level": typing.NotRequired[float | None],
    "help_flag": bool,
    "hist_flag": bool,
    "ver_flag": bool,
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
        "3dmaxima": v_3dmaxima_cargs,
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
        "3dmaxima": v_3dmaxima_outputs,
    }.get(t)


class V3dmaximaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmaxima(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_mask: OutputPathType | None
    """Output mask dataset with extrema locations"""


def v_3dmaxima_params(
    input_dataset: InputPathType,
    output_prefix: str | None = None,
    threshold: float | None = None,
    min_dist: float | None = None,
    out_rad: float | None = None,
    input_flag: bool = False,
    spheres_1_flag: bool = False,
    spheres_1to_n_flag: bool = False,
    spheres_nto1_flag: bool = False,
    neg_ext_flag: bool = False,
    true_max_flag: bool = False,
    dset_coords_flag: bool = False,
    no_text_flag: bool = False,
    coords_only_flag: bool = False,
    n_style_sort_flag: bool = False,
    n_style_weight_ave_flag: bool = False,
    debug_level: float | None = None,
    help_flag: bool = False,
    hist_flag: bool = False,
    ver_flag: bool = False,
) -> V3dmaximaParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Specify input dataset (e.g. func+orig'[7]').
        output_prefix: Prefix for an output mask dataset (e.g. -prefix\
            maskNto1).
        threshold: Provides a cutoff value for extrema (e.g. -thresh 17.4).
        min_dist: Minimum acceptable distance between extrema in voxels (e.g.\
            -min_dist 4).
        out_rad: Set the output radius around extrema voxels in voxel units\
            (e.g. -out_rad 9).
        input_flag: Specify input dataset (e.g. -input func+orig'[7]').
        spheres_1_flag: Set all output values to 1.
        spheres_1to_n_flag: Output values will range from 1 to N.
        spheres_nto1_flag: Output values will range from N to 1.
        neg_ext_flag: Search for negative extrema (minima).
        true_max_flag: Extrema may not have equal neighbors.
        dset_coords_flag: Display output in the dataset orientation.
        no_text_flag: Do not display the extrema points as text.
        coords_only_flag: Only output coordinates (no text or values).
        n_style_sort_flag: Use 'Sort-n-Remove' style (default).
        n_style_weight_ave_flag: Use 'Weighted-Average' style.
        debug_level: Output extra information to the terminal (e.g. -debug 2).
        help_flag: Display help information.
        hist_flag: Display module history.
        ver_flag: Display version number.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dmaxima",
        "input_dataset": input_dataset,
        "input_flag": input_flag,
        "spheres_1_flag": spheres_1_flag,
        "spheres_1toN_flag": spheres_1to_n_flag,
        "spheres_Nto1_flag": spheres_nto1_flag,
        "neg_ext_flag": neg_ext_flag,
        "true_max_flag": true_max_flag,
        "dset_coords_flag": dset_coords_flag,
        "no_text_flag": no_text_flag,
        "coords_only_flag": coords_only_flag,
        "n_style_sort_flag": n_style_sort_flag,
        "n_style_weight_ave_flag": n_style_weight_ave_flag,
        "help_flag": help_flag,
        "hist_flag": hist_flag,
        "ver_flag": ver_flag,
    }
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if threshold is not None:
        params["threshold"] = threshold
    if min_dist is not None:
        params["min_dist"] = min_dist
    if out_rad is not None:
        params["out_rad"] = out_rad
    if debug_level is not None:
        params["debug_level"] = debug_level
    return params


def v_3dmaxima_cargs(
    params: V3dmaximaParameters,
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
    cargs.append("3dmaxima")
    cargs.append(execution.input_file(params.get("input_dataset")))
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "-thresh",
            str(params.get("threshold"))
        ])
    if params.get("min_dist") is not None:
        cargs.extend([
            "-min_dist",
            str(params.get("min_dist"))
        ])
    if params.get("out_rad") is not None:
        cargs.extend([
            "-out_rad",
            str(params.get("out_rad"))
        ])
    if params.get("input_flag"):
        cargs.append("-input")
    if params.get("spheres_1_flag"):
        cargs.append("-spheres_1")
    if params.get("spheres_1toN_flag"):
        cargs.append("-spheres_1toN")
    if params.get("spheres_Nto1_flag"):
        cargs.append("-spheres_Nto1")
    if params.get("neg_ext_flag"):
        cargs.append("-neg_ext")
    if params.get("true_max_flag"):
        cargs.append("-true_max")
    if params.get("dset_coords_flag"):
        cargs.append("-dset_coords")
    if params.get("no_text_flag"):
        cargs.append("-no_text")
    if params.get("coords_only_flag"):
        cargs.append("-coords_only")
    if params.get("n_style_sort_flag"):
        cargs.append("-n_style_sort")
    if params.get("n_style_weight_ave_flag"):
        cargs.append("-n_style_weight_ave")
    if params.get("debug_level") is not None:
        cargs.extend([
            "-debug",
            str(params.get("debug_level"))
        ])
    if params.get("help_flag"):
        cargs.append("-help")
    if params.get("hist_flag"):
        cargs.append("-hist")
    if params.get("ver_flag"):
        cargs.append("-ver")
    return cargs


def v_3dmaxima_outputs(
    params: V3dmaximaParameters,
    execution: Execution,
) -> V3dmaximaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dmaximaOutputs(
        root=execution.output_file("."),
        output_mask=execution.output_file(params.get("output_prefix") + "_mask+orig.[HEAD | BRIK]") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def v_3dmaxima_execute(
    params: V3dmaximaParameters,
    execution: Execution,
) -> V3dmaximaOutputs:
    """
    Locate extrema in a functional dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dmaximaOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dmaxima_cargs(params, execution)
    ret = v_3dmaxima_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dmaxima(
    input_dataset: InputPathType,
    output_prefix: str | None = None,
    threshold: float | None = None,
    min_dist: float | None = None,
    out_rad: float | None = None,
    input_flag: bool = False,
    spheres_1_flag: bool = False,
    spheres_1to_n_flag: bool = False,
    spheres_nto1_flag: bool = False,
    neg_ext_flag: bool = False,
    true_max_flag: bool = False,
    dset_coords_flag: bool = False,
    no_text_flag: bool = False,
    coords_only_flag: bool = False,
    n_style_sort_flag: bool = False,
    n_style_weight_ave_flag: bool = False,
    debug_level: float | None = None,
    help_flag: bool = False,
    hist_flag: bool = False,
    ver_flag: bool = False,
    runner: Runner | None = None,
) -> V3dmaximaOutputs:
    """
    Locate extrema in a functional dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Specify input dataset (e.g. func+orig'[7]').
        output_prefix: Prefix for an output mask dataset (e.g. -prefix\
            maskNto1).
        threshold: Provides a cutoff value for extrema (e.g. -thresh 17.4).
        min_dist: Minimum acceptable distance between extrema in voxels (e.g.\
            -min_dist 4).
        out_rad: Set the output radius around extrema voxels in voxel units\
            (e.g. -out_rad 9).
        input_flag: Specify input dataset (e.g. -input func+orig'[7]').
        spheres_1_flag: Set all output values to 1.
        spheres_1to_n_flag: Output values will range from 1 to N.
        spheres_nto1_flag: Output values will range from N to 1.
        neg_ext_flag: Search for negative extrema (minima).
        true_max_flag: Extrema may not have equal neighbors.
        dset_coords_flag: Display output in the dataset orientation.
        no_text_flag: Do not display the extrema points as text.
        coords_only_flag: Only output coordinates (no text or values).
        n_style_sort_flag: Use 'Sort-n-Remove' style (default).
        n_style_weight_ave_flag: Use 'Weighted-Average' style.
        debug_level: Output extra information to the terminal (e.g. -debug 2).
        help_flag: Display help information.
        hist_flag: Display module history.
        ver_flag: Display version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmaximaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMAXIMA_METADATA)
    params = v_3dmaxima_params(
        input_dataset=input_dataset,
        output_prefix=output_prefix,
        threshold=threshold,
        min_dist=min_dist,
        out_rad=out_rad,
        input_flag=input_flag,
        spheres_1_flag=spheres_1_flag,
        spheres_1to_n_flag=spheres_1to_n_flag,
        spheres_nto1_flag=spheres_nto1_flag,
        neg_ext_flag=neg_ext_flag,
        true_max_flag=true_max_flag,
        dset_coords_flag=dset_coords_flag,
        no_text_flag=no_text_flag,
        coords_only_flag=coords_only_flag,
        n_style_sort_flag=n_style_sort_flag,
        n_style_weight_ave_flag=n_style_weight_ave_flag,
        debug_level=debug_level,
        help_flag=help_flag,
        hist_flag=hist_flag,
        ver_flag=ver_flag,
    )
    return v_3dmaxima_execute(params, execution)


__all__ = [
    "V3dmaximaOutputs",
    "V3dmaximaParameters",
    "V_3DMAXIMA_METADATA",
    "v_3dmaxima",
    "v_3dmaxima_params",
]
