# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_SETUP_GROUP_IN_CORR_METADATA = Metadata(
    id="f4fdb6eb2bdc0a77fec3e1f1a2cc5b51172322c2.boutiques",
    name="3dSetupGroupInCorr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dSetupGroupInCorrParameters = typing.TypedDict('V3dSetupGroupInCorrParameters', {
    "__STYX_TYPE__": typing.Literal["3dSetupGroupInCorr"],
    "datasets": list[InputPathType],
    "mask_dataset": typing.NotRequired[InputPathType | None],
    "prefix": str,
    "short_flag": bool,
    "byte_flag": bool,
    "labels_file": typing.NotRequired[InputPathType | None],
    "delete_flag": bool,
    "prep_method": typing.NotRequired[str | None],
    "lr_pairs": typing.NotRequired[list[str] | None],
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
        "3dSetupGroupInCorr": v_3d_setup_group_in_corr_cargs,
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
        "3dSetupGroupInCorr": v_3d_setup_group_in_corr_outputs,
    }.get(t)


class V3dSetupGroupInCorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_setup_group_in_corr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    niml_file: OutputPathType
    """Text file containing the header information describing the data file."""
    data_file: OutputPathType
    """Data file containing all the time series from all the datasets."""


def v_3d_setup_group_in_corr_params(
    datasets: list[InputPathType],
    prefix: str,
    mask_dataset: InputPathType | None = None,
    short_flag: bool = False,
    byte_flag: bool = False,
    labels_file: InputPathType | None = None,
    delete_flag: bool = False,
    prep_method: str | None = None,
    lr_pairs: list[str] | None = None,
) -> V3dSetupGroupInCorrParameters:
    """
    Build parameters.
    
    Args:
        datasets: AFNI 3D+time datasets to be processed.
        prefix: Prefix for output dataset names.
        mask_dataset: Mask dataset for voxel selection.
        short_flag: Store data as 16-bit shorts.
        byte_flag: Store data as 8-bit bytes.
        labels_file: File containing a list of labels for each dataset.
        delete_flag: Delete input datasets from disk after processing.
        prep_method: Preprocess each data time series with the specified\
            method.
        lr_pairs: Set the domains for left and right hemisphere surfaces and\
            indicate that the datasets are arranged in (Left, Right) pairs.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dSetupGroupInCorr",
        "datasets": datasets,
        "prefix": prefix,
        "short_flag": short_flag,
        "byte_flag": byte_flag,
        "delete_flag": delete_flag,
    }
    if mask_dataset is not None:
        params["mask_dataset"] = mask_dataset
    if labels_file is not None:
        params["labels_file"] = labels_file
    if prep_method is not None:
        params["prep_method"] = prep_method
    if lr_pairs is not None:
        params["lr_pairs"] = lr_pairs
    return params


def v_3d_setup_group_in_corr_cargs(
    params: V3dSetupGroupInCorrParameters,
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
    cargs.append("3dSetupGroupInCorr")
    cargs.extend([execution.input_file(f) for f in params.get("datasets")])
    if params.get("mask_dataset") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_dataset"))
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("short_flag"):
        cargs.append("-short")
    if params.get("byte_flag"):
        cargs.append("-byte")
    if params.get("labels_file") is not None:
        cargs.extend([
            "-labels",
            execution.input_file(params.get("labels_file"))
        ])
    if params.get("delete_flag"):
        cargs.append("-DELETE")
    if params.get("prep_method") is not None:
        cargs.extend([
            "-prep",
            params.get("prep_method")
        ])
    if params.get("lr_pairs") is not None:
        cargs.extend([
            "-LRpairs",
            *params.get("lr_pairs")
        ])
    return cargs


def v_3d_setup_group_in_corr_outputs(
    params: V3dSetupGroupInCorrParameters,
    execution: Execution,
) -> V3dSetupGroupInCorrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dSetupGroupInCorrOutputs(
        root=execution.output_file("."),
        niml_file=execution.output_file(params.get("prefix") + ".grpincorr.niml"),
        data_file=execution.output_file(params.get("prefix") + ".grpincorr.data"),
    )
    return ret


def v_3d_setup_group_in_corr_execute(
    params: V3dSetupGroupInCorrParameters,
    execution: Execution,
) -> V3dSetupGroupInCorrOutputs:
    """
    Pre-process a collection of AFNI 3D+time datasets for use with Group InstaCorr.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dSetupGroupInCorrOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_setup_group_in_corr_cargs(params, execution)
    ret = v_3d_setup_group_in_corr_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_setup_group_in_corr(
    datasets: list[InputPathType],
    prefix: str,
    mask_dataset: InputPathType | None = None,
    short_flag: bool = False,
    byte_flag: bool = False,
    labels_file: InputPathType | None = None,
    delete_flag: bool = False,
    prep_method: str | None = None,
    lr_pairs: list[str] | None = None,
    runner: Runner | None = None,
) -> V3dSetupGroupInCorrOutputs:
    """
    Pre-process a collection of AFNI 3D+time datasets for use with Group InstaCorr.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        datasets: AFNI 3D+time datasets to be processed.
        prefix: Prefix for output dataset names.
        mask_dataset: Mask dataset for voxel selection.
        short_flag: Store data as 16-bit shorts.
        byte_flag: Store data as 8-bit bytes.
        labels_file: File containing a list of labels for each dataset.
        delete_flag: Delete input datasets from disk after processing.
        prep_method: Preprocess each data time series with the specified\
            method.
        lr_pairs: Set the domains for left and right hemisphere surfaces and\
            indicate that the datasets are arranged in (Left, Right) pairs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSetupGroupInCorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SETUP_GROUP_IN_CORR_METADATA)
    params = v_3d_setup_group_in_corr_params(
        datasets=datasets,
        mask_dataset=mask_dataset,
        prefix=prefix,
        short_flag=short_flag,
        byte_flag=byte_flag,
        labels_file=labels_file,
        delete_flag=delete_flag,
        prep_method=prep_method,
        lr_pairs=lr_pairs,
    )
    return v_3d_setup_group_in_corr_execute(params, execution)


__all__ = [
    "V3dSetupGroupInCorrOutputs",
    "V3dSetupGroupInCorrParameters",
    "V_3D_SETUP_GROUP_IN_CORR_METADATA",
    "v_3d_setup_group_in_corr",
    "v_3d_setup_group_in_corr_params",
]
