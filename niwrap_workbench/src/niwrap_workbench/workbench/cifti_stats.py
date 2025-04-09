# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_STATS_METADATA = Metadata(
    id="59510ec6fa9ccb15b91394912ea55ac86e9579d7.boutiques",
    name="cifti-stats",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


CiftiStatsRoiParameters = typing.TypedDict('CiftiStatsRoiParameters', {
    "__STYX_TYPE__": typing.Literal["roi"],
    "roi_cifti": InputPathType,
    "opt_match_maps": bool,
})


CiftiStatsParameters = typing.TypedDict('CiftiStatsParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-stats"],
    "cifti_in": InputPathType,
    "opt_reduce_operation": typing.NotRequired[str | None],
    "opt_percentile_percent": typing.NotRequired[float | None],
    "opt_column_column": typing.NotRequired[int | None],
    "roi": typing.NotRequired[CiftiStatsRoiParameters | None],
    "opt_show_map_name": bool,
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
        "cifti-stats": cifti_stats_cargs,
        "roi": cifti_stats_roi_cargs,
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
    }.get(t)


def cifti_stats_roi_params(
    roi_cifti: InputPathType,
    opt_match_maps: bool = False,
) -> CiftiStatsRoiParameters:
    """
    Build parameters.
    
    Args:
        roi_cifti: the roi, as a cifti file.
        opt_match_maps: each column of input uses the corresponding column from\
            the roi file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "roi",
        "roi_cifti": roi_cifti,
        "opt_match_maps": opt_match_maps,
    }
    return params


def cifti_stats_roi_cargs(
    params: CiftiStatsRoiParameters,
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
    cargs.append("-roi")
    cargs.append(execution.input_file(params.get("roi_cifti")))
    if params.get("opt_match_maps"):
        cargs.append("-match-maps")
    return cargs


class CiftiStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_stats_params(
    cifti_in: InputPathType,
    opt_reduce_operation: str | None = None,
    opt_percentile_percent: float | None = None,
    opt_column_column: int | None = None,
    roi: CiftiStatsRoiParameters | None = None,
    opt_show_map_name: bool = False,
) -> CiftiStatsParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: the input cifti.
        opt_reduce_operation: use a reduction operation: the reduction\
            operation.
        opt_percentile_percent: give the value at a percentile: the percentile\
            to find, must be between 0 and 100.
        opt_column_column: only display output for one column: the column index\
            (starting from 1).
        roi: only consider data inside an roi.
        opt_show_map_name: print column index and name before each output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-stats",
        "cifti_in": cifti_in,
        "opt_show_map_name": opt_show_map_name,
    }
    if opt_reduce_operation is not None:
        params["opt_reduce_operation"] = opt_reduce_operation
    if opt_percentile_percent is not None:
        params["opt_percentile_percent"] = opt_percentile_percent
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if roi is not None:
        params["roi"] = roi
    return params


def cifti_stats_cargs(
    params: CiftiStatsParameters,
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
    cargs.append("-cifti-stats")
    cargs.append(execution.input_file(params.get("cifti_in")))
    if params.get("opt_reduce_operation") is not None:
        cargs.extend([
            "-reduce",
            params.get("opt_reduce_operation")
        ])
    if params.get("opt_percentile_percent") is not None:
        cargs.extend([
            "-percentile",
            str(params.get("opt_percentile_percent"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            str(params.get("opt_column_column"))
        ])
    if params.get("roi") is not None:
        cargs.extend(dyn_cargs(params.get("roi")["__STYXTYPE__"])(params.get("roi"), execution))
    if params.get("opt_show_map_name"):
        cargs.append("-show-map-name")
    return cargs


def cifti_stats_outputs(
    params: CiftiStatsParameters,
    execution: Execution,
) -> CiftiStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiStatsOutputs(
        root=execution.output_file("."),
    )
    return ret


def cifti_stats_execute(
    params: CiftiStatsParameters,
    execution: Execution,
) -> CiftiStatsOutputs:
    """
    Statistics along cifti columns.
    
    For each column of the input, a line of text is printed, resulting from the
    specified reduction or percentile operation. If -roi is specified without
    -match-maps, then each line will contain as many numbers as there are maps
    in the ROI file, separated by tab characters. Use -column to only give
    output for a single data column. Exactly one of -reduce or -percentile must
    be specified.
    
    The argument to the -reduce option must be one of the following:
    
    MAX: the maximum value
    MIN: the minimum value
    INDEXMAX: the 1-based index of the maximum value
    INDEXMIN: the 1-based index of the minimum value
    SUM: add all values
    PRODUCT: multiply all values
    MEAN: the mean of the data
    STDEV: the standard deviation (N denominator)
    SAMPSTDEV: the sample standard deviation (N-1 denominator)
    VARIANCE: the variance of the data
    TSNR: mean divided by sample standard deviation (N-1 denominator)
    COV: sample standard deviation (N-1 denominator) divided by mean
    L2NORM: square root of sum of squares
    MEDIAN: the median of the data
    MODE: the mode of the data
    COUNT_NONZERO: the number of nonzero elements in the data
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiStatsOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_stats_cargs(params, execution)
    ret = cifti_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_stats(
    cifti_in: InputPathType,
    opt_reduce_operation: str | None = None,
    opt_percentile_percent: float | None = None,
    opt_column_column: int | None = None,
    roi: CiftiStatsRoiParameters | None = None,
    opt_show_map_name: bool = False,
    runner: Runner | None = None,
) -> CiftiStatsOutputs:
    """
    Statistics along cifti columns.
    
    For each column of the input, a line of text is printed, resulting from the
    specified reduction or percentile operation. If -roi is specified without
    -match-maps, then each line will contain as many numbers as there are maps
    in the ROI file, separated by tab characters. Use -column to only give
    output for a single data column. Exactly one of -reduce or -percentile must
    be specified.
    
    The argument to the -reduce option must be one of the following:
    
    MAX: the maximum value
    MIN: the minimum value
    INDEXMAX: the 1-based index of the maximum value
    INDEXMIN: the 1-based index of the minimum value
    SUM: add all values
    PRODUCT: multiply all values
    MEAN: the mean of the data
    STDEV: the standard deviation (N denominator)
    SAMPSTDEV: the sample standard deviation (N-1 denominator)
    VARIANCE: the variance of the data
    TSNR: mean divided by sample standard deviation (N-1 denominator)
    COV: sample standard deviation (N-1 denominator) divided by mean
    L2NORM: square root of sum of squares
    MEDIAN: the median of the data
    MODE: the mode of the data
    COUNT_NONZERO: the number of nonzero elements in the data
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the input cifti.
        opt_reduce_operation: use a reduction operation: the reduction\
            operation.
        opt_percentile_percent: give the value at a percentile: the percentile\
            to find, must be between 0 and 100.
        opt_column_column: only display output for one column: the column index\
            (starting from 1).
        roi: only consider data inside an roi.
        opt_show_map_name: print column index and name before each output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_STATS_METADATA)
    params = cifti_stats_params(
        cifti_in=cifti_in,
        opt_reduce_operation=opt_reduce_operation,
        opt_percentile_percent=opt_percentile_percent,
        opt_column_column=opt_column_column,
        roi=roi,
        opt_show_map_name=opt_show_map_name,
    )
    return cifti_stats_execute(params, execution)


__all__ = [
    "CIFTI_STATS_METADATA",
    "CiftiStatsOutputs",
    "CiftiStatsParameters",
    "CiftiStatsRoiParameters",
    "cifti_stats",
    "cifti_stats_params",
    "cifti_stats_roi_params",
]
