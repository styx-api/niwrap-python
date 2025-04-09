# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_NET_CORR_METADATA = Metadata(
    id="5670b5b4f9d0ab3696cc0b14e6eaa44805f1ab6c.boutiques",
    name="3dNetCorr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dNetCorrParameters = typing.TypedDict('V3dNetCorrParameters', {
    "__STYX_TYPE__": typing.Literal["3dNetCorr"],
    "prefix": str,
    "inset": InputPathType,
    "in_rois": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "fish_z": bool,
    "part_corr": bool,
    "ts_out": bool,
    "ts_label": bool,
    "ts_indiv": bool,
    "ts_wb_corr": bool,
    "ts_wb_Z": bool,
    "weight_ts": typing.NotRequired[InputPathType | None],
    "weight_corr": typing.NotRequired[InputPathType | None],
    "ts_wb_strlabel": bool,
    "nifti": bool,
    "output_mask_nonnull": bool,
    "push_thru_many_zeros": bool,
    "allow_roi_zeros": bool,
    "automask_off": bool,
    "ignore_LT": bool,
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
        "3dNetCorr": v_3d_net_corr_cargs,
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
        "3dNetCorr": v_3d_net_corr_outputs,
    }.get(t)


class V3dNetCorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_net_corr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_netcc: OutputPathType
    """Output correlation matrix file for network 000"""
    output_netts: OutputPathType
    """Output mean time series per ROI for network 000"""
    output_niml: OutputPathType
    """NIML/SUMA-esque file for visualizing connectivity info in a 3D brain for
    network 000"""
    output_roidat: OutputPathType
    """Columns contain information for each ROI in the used mask."""
    output_mask_nnull: OutputPathType
    """Mask of non-null time series"""
    output_indiv: OutputPathType
    """Directory containing individual time series files for network 000"""
    output_binary_mask_nnull: OutputPathType
    """Binary mask of the non-null time series"""


def v_3d_net_corr_params(
    prefix: str,
    inset: InputPathType,
    in_rois: InputPathType,
    mask: InputPathType | None = None,
    fish_z: bool = False,
    part_corr: bool = False,
    ts_out: bool = False,
    ts_label: bool = False,
    ts_indiv: bool = False,
    ts_wb_corr: bool = False,
    ts_wb_z: bool = False,
    weight_ts: InputPathType | None = None,
    weight_corr: InputPathType | None = None,
    ts_wb_strlabel: bool = False,
    nifti: bool = False,
    output_mask_nonnull: bool = False,
    push_thru_many_zeros: bool = False,
    allow_roi_zeros: bool = False,
    automask_off: bool = False,
    ignore_lt: bool = False,
) -> V3dNetCorrParameters:
    """
    Build parameters.
    
    Args:
        prefix: Output file name prefix.
        inset: Time series file (4D data set).
        in_rois: Input a set of ROIs each labelled with distinct integers.\
            Multiple subbricks can be input, each will be treated as a separate\
            network.
        mask: Whole brain mask within which to calculate correlation.
        fish_z: Output Fisher Z-transform matrix along with correlation matrix.
        part_corr: Output the partial correlation matrix.
        ts_out: Output the mean time series of the ROIs.
        ts_label: Insert the integer ROI label at the start of each line of the\
            *.netts file created.
        ts_indiv: Create a directory for each network that contains the average\
            time series for each ROI in individual files.
        ts_wb_corr: Perform whole brain correlation for each ROI's average time\
            series and output as Pearson 'r' values.
        ts_wb_z: Perform whole brain correlation for each ROI's average time\
            series and output as Fisher transformed Z-scores.
        weight_ts: Input a 1D file of weights to be applied multiplicatively to\
            each ROI's average time series.
        weight_corr: Input a 1D file of weights to estimate a weighted Pearson\
            Correlation.
        ts_wb_strlabel: Apply string labels to the WB correlation/Z-score\
            output files.
        nifti: Output any correlation map files as NIFTI files.
        output_mask_nonnull: Output mask of non-null time series.
        push_thru_many_zeros: Push through the calculation even if any ROI\
            contains more than 10 percent of voxels with null time series.
        allow_roi_zeros: Allow ROIs to have all-zero time series.
        automask_off: Disable internal automasking of where time series are not\
            uniformly zero.
        ignore_lt: Ignore any label table labels in the '-in_rois' file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dNetCorr",
        "prefix": prefix,
        "inset": inset,
        "in_rois": in_rois,
        "fish_z": fish_z,
        "part_corr": part_corr,
        "ts_out": ts_out,
        "ts_label": ts_label,
        "ts_indiv": ts_indiv,
        "ts_wb_corr": ts_wb_corr,
        "ts_wb_Z": ts_wb_z,
        "ts_wb_strlabel": ts_wb_strlabel,
        "nifti": nifti,
        "output_mask_nonnull": output_mask_nonnull,
        "push_thru_many_zeros": push_thru_many_zeros,
        "allow_roi_zeros": allow_roi_zeros,
        "automask_off": automask_off,
        "ignore_LT": ignore_lt,
    }
    if mask is not None:
        params["mask"] = mask
    if weight_ts is not None:
        params["weight_ts"] = weight_ts
    if weight_corr is not None:
        params["weight_corr"] = weight_corr
    return params


def v_3d_net_corr_cargs(
    params: V3dNetCorrParameters,
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
    cargs.append("3dNetCorr")
    cargs.append(params.get("prefix"))
    cargs.append(execution.input_file(params.get("inset")))
    cargs.append(execution.input_file(params.get("in_rois")))
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("fish_z"):
        cargs.append("-fish_z")
    if params.get("part_corr"):
        cargs.append("-part_corr")
    if params.get("ts_out"):
        cargs.append("-ts_out")
    if params.get("ts_label"):
        cargs.append("-ts_label")
    if params.get("ts_indiv"):
        cargs.append("-ts_indiv")
    if params.get("ts_wb_corr"):
        cargs.append("-ts_wb_corr")
    if params.get("ts_wb_Z"):
        cargs.append("-ts_wb_Z")
    if params.get("weight_ts") is not None:
        cargs.extend([
            "-weight_ts",
            execution.input_file(params.get("weight_ts"))
        ])
    if params.get("weight_corr") is not None:
        cargs.extend([
            "-weight_corr",
            execution.input_file(params.get("weight_corr"))
        ])
    if params.get("ts_wb_strlabel"):
        cargs.append("-ts_wb_strlabel")
    if params.get("nifti"):
        cargs.append("-nifti")
    if params.get("output_mask_nonnull"):
        cargs.append("-output_mask_nonnull")
    if params.get("push_thru_many_zeros"):
        cargs.append("-push_thru_many_zeros")
    if params.get("allow_roi_zeros"):
        cargs.append("-allow_roi_zeros")
    if params.get("automask_off"):
        cargs.append("-automask_off")
    if params.get("ignore_LT"):
        cargs.append("-ignore_LT")
    return cargs


def v_3d_net_corr_outputs(
    params: V3dNetCorrParameters,
    execution: Execution,
) -> V3dNetCorrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dNetCorrOutputs(
        root=execution.output_file("."),
        output_netcc=execution.output_file(params.get("prefix") + "_000.netcc"),
        output_netts=execution.output_file(params.get("prefix") + "_000.netts"),
        output_niml=execution.output_file(params.get("prefix") + "_000.niml.dset"),
        output_roidat=execution.output_file(params.get("prefix") + ".roidat"),
        output_mask_nnull=execution.output_file(params.get("prefix") + "_mask_nnull"),
        output_indiv=execution.output_file(params.get("prefix") + "_000_INDIV"),
        output_binary_mask_nnull=execution.output_file("PREFIX_mask_nnull"),
    )
    return ret


def v_3d_net_corr_execute(
    params: V3dNetCorrParameters,
    execution: Execution,
) -> V3dNetCorrOutputs:
    """
    Compute correlation matrix of a set of ROIs based on mean time series.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dNetCorrOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_net_corr_cargs(params, execution)
    ret = v_3d_net_corr_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_net_corr(
    prefix: str,
    inset: InputPathType,
    in_rois: InputPathType,
    mask: InputPathType | None = None,
    fish_z: bool = False,
    part_corr: bool = False,
    ts_out: bool = False,
    ts_label: bool = False,
    ts_indiv: bool = False,
    ts_wb_corr: bool = False,
    ts_wb_z: bool = False,
    weight_ts: InputPathType | None = None,
    weight_corr: InputPathType | None = None,
    ts_wb_strlabel: bool = False,
    nifti: bool = False,
    output_mask_nonnull: bool = False,
    push_thru_many_zeros: bool = False,
    allow_roi_zeros: bool = False,
    automask_off: bool = False,
    ignore_lt: bool = False,
    runner: Runner | None = None,
) -> V3dNetCorrOutputs:
    """
    Compute correlation matrix of a set of ROIs based on mean time series.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Output file name prefix.
        inset: Time series file (4D data set).
        in_rois: Input a set of ROIs each labelled with distinct integers.\
            Multiple subbricks can be input, each will be treated as a separate\
            network.
        mask: Whole brain mask within which to calculate correlation.
        fish_z: Output Fisher Z-transform matrix along with correlation matrix.
        part_corr: Output the partial correlation matrix.
        ts_out: Output the mean time series of the ROIs.
        ts_label: Insert the integer ROI label at the start of each line of the\
            *.netts file created.
        ts_indiv: Create a directory for each network that contains the average\
            time series for each ROI in individual files.
        ts_wb_corr: Perform whole brain correlation for each ROI's average time\
            series and output as Pearson 'r' values.
        ts_wb_z: Perform whole brain correlation for each ROI's average time\
            series and output as Fisher transformed Z-scores.
        weight_ts: Input a 1D file of weights to be applied multiplicatively to\
            each ROI's average time series.
        weight_corr: Input a 1D file of weights to estimate a weighted Pearson\
            Correlation.
        ts_wb_strlabel: Apply string labels to the WB correlation/Z-score\
            output files.
        nifti: Output any correlation map files as NIFTI files.
        output_mask_nonnull: Output mask of non-null time series.
        push_thru_many_zeros: Push through the calculation even if any ROI\
            contains more than 10 percent of voxels with null time series.
        allow_roi_zeros: Allow ROIs to have all-zero time series.
        automask_off: Disable internal automasking of where time series are not\
            uniformly zero.
        ignore_lt: Ignore any label table labels in the '-in_rois' file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dNetCorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_NET_CORR_METADATA)
    params = v_3d_net_corr_params(
        prefix=prefix,
        inset=inset,
        in_rois=in_rois,
        mask=mask,
        fish_z=fish_z,
        part_corr=part_corr,
        ts_out=ts_out,
        ts_label=ts_label,
        ts_indiv=ts_indiv,
        ts_wb_corr=ts_wb_corr,
        ts_wb_z=ts_wb_z,
        weight_ts=weight_ts,
        weight_corr=weight_corr,
        ts_wb_strlabel=ts_wb_strlabel,
        nifti=nifti,
        output_mask_nonnull=output_mask_nonnull,
        push_thru_many_zeros=push_thru_many_zeros,
        allow_roi_zeros=allow_roi_zeros,
        automask_off=automask_off,
        ignore_lt=ignore_lt,
    )
    return v_3d_net_corr_execute(params, execution)


__all__ = [
    "V3dNetCorrOutputs",
    "V3dNetCorrParameters",
    "V_3D_NET_CORR_METADATA",
    "v_3d_net_corr",
    "v_3d_net_corr_params",
]
