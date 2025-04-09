# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_CURVATURE_STATS_METADATA = Metadata(
    id="bca36cbb94236a4f6fd00f26206b719765aa2bb6.boutiques",
    name="mris_curvature_stats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisCurvatureStatsParameters = typing.TypedDict('MrisCurvatureStatsParameters', {
    "__STYX_TYPE__": typing.Literal["mris_curvature_stats"],
    "subject_name": str,
    "hemisphere": str,
    "curvature_files": typing.NotRequired[list[InputPathType] | None],
    "number_of_averages": typing.NotRequired[float | None],
    "principal_curvatures": bool,
    "discrete_method": bool,
    "continuous_method": bool,
    "signed_principals": bool,
    "vertex_area_weigh": bool,
    "vertex_area_normalize": bool,
    "vertex_area_weigh_frac": bool,
    "vertex_area_normalize_frac": bool,
    "post_scale": typing.NotRequired[float | None],
    "write_curvature_files": bool,
    "shape_index": bool,
    "output_file_stem": typing.NotRequired[str | None],
    "histogram_bins": typing.NotRequired[float | None],
    "percentage_histogram_bins": typing.NotRequired[float | None],
    "bin_size": typing.NotRequired[float | None],
    "bin_start_curvature": typing.NotRequired[float | None],
    "bin_end_curvature": typing.NotRequired[float | None],
    "label_file": typing.NotRequired[InputPathType | None],
    "regional_percentages": bool,
    "high_pass_filter": typing.NotRequired[float | None],
    "low_pass_filter": typing.NotRequired[float | None],
    "high_pass_filter_gaussian": typing.NotRequired[float | None],
    "low_pass_filter_gaussian": typing.NotRequired[float | None],
    "filter_label": typing.NotRequired[InputPathType | None],
    "min_max_info": bool,
    "normalize_curvature": bool,
    "summary_condition": typing.NotRequired[str | None],
    "min_curvature_scale": typing.NotRequired[float | None],
    "max_curvature_scale": typing.NotRequired[float | None],
    "scale_factor": typing.NotRequired[float | None],
    "version": bool,
    "set_zero_vertex": typing.NotRequired[float | None],
    "max_ulps": typing.NotRequired[float | None],
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
        "mris_curvature_stats": mris_curvature_stats_cargs,
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


class MrisCurvatureStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_curvature_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_curvature_stats_params(
    subject_name: str,
    hemisphere: str,
    curvature_files: list[InputPathType] | None = None,
    number_of_averages: float | None = None,
    principal_curvatures: bool = False,
    discrete_method: bool = False,
    continuous_method: bool = False,
    signed_principals: bool = False,
    vertex_area_weigh: bool = False,
    vertex_area_normalize: bool = False,
    vertex_area_weigh_frac: bool = False,
    vertex_area_normalize_frac: bool = False,
    post_scale: float | None = None,
    write_curvature_files: bool = False,
    shape_index: bool = False,
    output_file_stem: str | None = None,
    histogram_bins: float | None = None,
    percentage_histogram_bins: float | None = None,
    bin_size: float | None = None,
    bin_start_curvature: float | None = None,
    bin_end_curvature: float | None = None,
    label_file: InputPathType | None = None,
    regional_percentages: bool = False,
    high_pass_filter: float | None = None,
    low_pass_filter: float | None = None,
    high_pass_filter_gaussian: float | None = None,
    low_pass_filter_gaussian: float | None = None,
    filter_label: InputPathType | None = None,
    min_max_info: bool = False,
    normalize_curvature: bool = False,
    summary_condition: str | None = None,
    min_curvature_scale: float | None = None,
    max_curvature_scale: float | None = None,
    scale_factor: float | None = None,
    version: bool = False,
    set_zero_vertex: float | None = None,
    max_ulps: float | None = None,
) -> MrisCurvatureStatsParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Subject name defined in the SUBJECTS_DIR.
        hemisphere: Hemisphere, can be 'lh' or 'rh'.
        curvature_files: Optional list of curvature files to process.
        number_of_averages: Average the curvature number of times.
        principal_curvatures: Calculate principal curvatures and derived maps.
        discrete_method: Use discrete calculation method for principal\
            curvatures.
        continuous_method: Use continuous calculation method for principal\
            curvatures.
        signed_principals: Assign signed max and min to principal curvature K1\
            and K2.
        vertex_area_weigh: Multiply curvature value by the area of its vertex.
        vertex_area_normalize: Divide curvature value by the area of its\
            vertex.
        vertex_area_weigh_frac: Weigh curvature by the fractional vertex area.
        vertex_area_normalize_frac: Normalize curvature by the fractional\
            vertex area.
        post_scale: Scale the mean and areaNorm integrals by a factor.
        write_curvature_files: Write the calculated curvature values to files\
            in FreeSurfer format.
        shape_index: Calculate shape index despite potential atan issues.
        output_file_stem: Output file stem for results.
        histogram_bins: Number of bins for curvature histogram.
        percentage_histogram_bins: Number of bins for percentage-based\
            curvature histogram.
        bin_size: Size of each histogram bin.
        bin_start_curvature: Histogram bin start value.
        bin_end_curvature: Histogram bin end value.
        label_file: Label file to constrain statistics to a region.
        regional_percentages: Report integral percentages relative to the\
            region.
        high_pass_filter: High pass filter for curvature values.
        low_pass_filter: Low pass filter for curvature values.
        high_pass_filter_gaussian: High pass filter for Gaussian curvature\
            values.
        low_pass_filter_gaussian: Low pass filter for Gaussian curvature\
            values.
        filter_label: Store processed surface vertices in a label file.
        min_max_info: Output min/max information for the processed curvature.
        normalize_curvature: Normalize the curvature before computation.
        summary_condition: Write out stats as a summary condition.
        min_curvature_scale: Scale curvature values between min and max\
            curvature.
        max_curvature_scale: End value for curvature scaling.
        scale_factor: Scale curvature values with a factor.
        version: Print out version number.
        set_zero_vertex: Sets the curvature values at that index to zero.
        max_ulps: Toggle a more rigorous floating point comparison operation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_curvature_stats",
        "subject_name": subject_name,
        "hemisphere": hemisphere,
        "principal_curvatures": principal_curvatures,
        "discrete_method": discrete_method,
        "continuous_method": continuous_method,
        "signed_principals": signed_principals,
        "vertex_area_weigh": vertex_area_weigh,
        "vertex_area_normalize": vertex_area_normalize,
        "vertex_area_weigh_frac": vertex_area_weigh_frac,
        "vertex_area_normalize_frac": vertex_area_normalize_frac,
        "write_curvature_files": write_curvature_files,
        "shape_index": shape_index,
        "regional_percentages": regional_percentages,
        "min_max_info": min_max_info,
        "normalize_curvature": normalize_curvature,
        "version": version,
    }
    if curvature_files is not None:
        params["curvature_files"] = curvature_files
    if number_of_averages is not None:
        params["number_of_averages"] = number_of_averages
    if post_scale is not None:
        params["post_scale"] = post_scale
    if output_file_stem is not None:
        params["output_file_stem"] = output_file_stem
    if histogram_bins is not None:
        params["histogram_bins"] = histogram_bins
    if percentage_histogram_bins is not None:
        params["percentage_histogram_bins"] = percentage_histogram_bins
    if bin_size is not None:
        params["bin_size"] = bin_size
    if bin_start_curvature is not None:
        params["bin_start_curvature"] = bin_start_curvature
    if bin_end_curvature is not None:
        params["bin_end_curvature"] = bin_end_curvature
    if label_file is not None:
        params["label_file"] = label_file
    if high_pass_filter is not None:
        params["high_pass_filter"] = high_pass_filter
    if low_pass_filter is not None:
        params["low_pass_filter"] = low_pass_filter
    if high_pass_filter_gaussian is not None:
        params["high_pass_filter_gaussian"] = high_pass_filter_gaussian
    if low_pass_filter_gaussian is not None:
        params["low_pass_filter_gaussian"] = low_pass_filter_gaussian
    if filter_label is not None:
        params["filter_label"] = filter_label
    if summary_condition is not None:
        params["summary_condition"] = summary_condition
    if min_curvature_scale is not None:
        params["min_curvature_scale"] = min_curvature_scale
    if max_curvature_scale is not None:
        params["max_curvature_scale"] = max_curvature_scale
    if scale_factor is not None:
        params["scale_factor"] = scale_factor
    if set_zero_vertex is not None:
        params["set_zero_vertex"] = set_zero_vertex
    if max_ulps is not None:
        params["max_ulps"] = max_ulps
    return params


def mris_curvature_stats_cargs(
    params: MrisCurvatureStatsParameters,
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
    cargs.append("mris_curvature_stats")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemisphere"))
    if params.get("curvature_files") is not None:
        cargs.extend([execution.input_file(f) for f in params.get("curvature_files")])
    if params.get("number_of_averages") is not None:
        cargs.extend([
            "-a",
            str(params.get("number_of_averages"))
        ])
    if params.get("principal_curvatures"):
        cargs.append("-G")
    if params.get("discrete_method"):
        cargs.append("--discrete")
    if params.get("continuous_method"):
        cargs.append("--continuous")
    if params.get("signed_principals"):
        cargs.append("--signedPrincipals")
    if params.get("vertex_area_weigh"):
        cargs.append("--vertexAreaWeigh")
    if params.get("vertex_area_normalize"):
        cargs.append("--vertexAreaNormalize")
    if params.get("vertex_area_weigh_frac"):
        cargs.append("--vertexAreaWeighFrac")
    if params.get("vertex_area_normalize_frac"):
        cargs.append("--vertexAreaNormalizeFrac")
    if params.get("post_scale") is not None:
        cargs.extend([
            "--postScale",
            str(params.get("post_scale"))
        ])
    if params.get("write_curvature_files"):
        cargs.append("--writeCurvatureFiles")
    if params.get("shape_index"):
        cargs.append("--shapeIndex")
    if params.get("output_file_stem") is not None:
        cargs.extend([
            "-o",
            params.get("output_file_stem")
        ])
    if params.get("histogram_bins") is not None:
        cargs.extend([
            "-h",
            str(params.get("histogram_bins"))
        ])
    if params.get("percentage_histogram_bins") is not None:
        cargs.extend([
            "-p",
            str(params.get("percentage_histogram_bins"))
        ])
    if params.get("bin_size") is not None:
        cargs.extend([
            "-b",
            str(params.get("bin_size"))
        ])
    if params.get("bin_start_curvature") is not None:
        cargs.extend([
            "-i",
            str(params.get("bin_start_curvature"))
        ])
    if params.get("bin_end_curvature") is not None:
        cargs.extend([
            "-j",
            str(params.get("bin_end_curvature"))
        ])
    if params.get("label_file") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("label_file"))
        ])
    if params.get("regional_percentages"):
        cargs.append("--regionalPercentages")
    if params.get("high_pass_filter") is not None:
        cargs.extend([
            "--highPassFilter",
            str(params.get("high_pass_filter"))
        ])
    if params.get("low_pass_filter") is not None:
        cargs.extend([
            "--lowPassFilter",
            str(params.get("low_pass_filter"))
        ])
    if params.get("high_pass_filter_gaussian") is not None:
        cargs.extend([
            "--highPassFilterGaussian",
            str(params.get("high_pass_filter_gaussian"))
        ])
    if params.get("low_pass_filter_gaussian") is not None:
        cargs.extend([
            "--lowPassFilterGaussian",
            str(params.get("low_pass_filter_gaussian"))
        ])
    if params.get("filter_label") is not None:
        cargs.extend([
            "--filterLabel",
            execution.input_file(params.get("filter_label"))
        ])
    if params.get("min_max_info"):
        cargs.append("-m")
    if params.get("normalize_curvature"):
        cargs.append("-n")
    if params.get("summary_condition") is not None:
        cargs.extend([
            "-s",
            params.get("summary_condition")
        ])
    if params.get("min_curvature_scale") is not None:
        cargs.extend([
            "-d",
            str(params.get("min_curvature_scale"))
        ])
    if params.get("max_curvature_scale") is not None:
        cargs.extend([
            "-e",
            str(params.get("max_curvature_scale"))
        ])
    if params.get("scale_factor") is not None:
        cargs.extend([
            "-c",
            str(params.get("scale_factor"))
        ])
    if params.get("version"):
        cargs.append("-version")
    if params.get("set_zero_vertex") is not None:
        cargs.extend([
            "-z",
            str(params.get("set_zero_vertex"))
        ])
    if params.get("max_ulps") is not None:
        cargs.extend([
            "-q",
            str(params.get("max_ulps"))
        ])
    return cargs


def mris_curvature_stats_outputs(
    params: MrisCurvatureStatsParameters,
    execution: Execution,
) -> MrisCurvatureStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisCurvatureStatsOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_curvature_stats_execute(
    params: MrisCurvatureStatsParameters,
    execution: Execution,
) -> MrisCurvatureStatsOutputs:
    """
    Tool for calculating statistics on surface curvature values.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisCurvatureStatsOutputs`).
    """
    params = execution.params(params)
    cargs = mris_curvature_stats_cargs(params, execution)
    ret = mris_curvature_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_curvature_stats(
    subject_name: str,
    hemisphere: str,
    curvature_files: list[InputPathType] | None = None,
    number_of_averages: float | None = None,
    principal_curvatures: bool = False,
    discrete_method: bool = False,
    continuous_method: bool = False,
    signed_principals: bool = False,
    vertex_area_weigh: bool = False,
    vertex_area_normalize: bool = False,
    vertex_area_weigh_frac: bool = False,
    vertex_area_normalize_frac: bool = False,
    post_scale: float | None = None,
    write_curvature_files: bool = False,
    shape_index: bool = False,
    output_file_stem: str | None = None,
    histogram_bins: float | None = None,
    percentage_histogram_bins: float | None = None,
    bin_size: float | None = None,
    bin_start_curvature: float | None = None,
    bin_end_curvature: float | None = None,
    label_file: InputPathType | None = None,
    regional_percentages: bool = False,
    high_pass_filter: float | None = None,
    low_pass_filter: float | None = None,
    high_pass_filter_gaussian: float | None = None,
    low_pass_filter_gaussian: float | None = None,
    filter_label: InputPathType | None = None,
    min_max_info: bool = False,
    normalize_curvature: bool = False,
    summary_condition: str | None = None,
    min_curvature_scale: float | None = None,
    max_curvature_scale: float | None = None,
    scale_factor: float | None = None,
    version: bool = False,
    set_zero_vertex: float | None = None,
    max_ulps: float | None = None,
    runner: Runner | None = None,
) -> MrisCurvatureStatsOutputs:
    """
    Tool for calculating statistics on surface curvature values.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Subject name defined in the SUBJECTS_DIR.
        hemisphere: Hemisphere, can be 'lh' or 'rh'.
        curvature_files: Optional list of curvature files to process.
        number_of_averages: Average the curvature number of times.
        principal_curvatures: Calculate principal curvatures and derived maps.
        discrete_method: Use discrete calculation method for principal\
            curvatures.
        continuous_method: Use continuous calculation method for principal\
            curvatures.
        signed_principals: Assign signed max and min to principal curvature K1\
            and K2.
        vertex_area_weigh: Multiply curvature value by the area of its vertex.
        vertex_area_normalize: Divide curvature value by the area of its\
            vertex.
        vertex_area_weigh_frac: Weigh curvature by the fractional vertex area.
        vertex_area_normalize_frac: Normalize curvature by the fractional\
            vertex area.
        post_scale: Scale the mean and areaNorm integrals by a factor.
        write_curvature_files: Write the calculated curvature values to files\
            in FreeSurfer format.
        shape_index: Calculate shape index despite potential atan issues.
        output_file_stem: Output file stem for results.
        histogram_bins: Number of bins for curvature histogram.
        percentage_histogram_bins: Number of bins for percentage-based\
            curvature histogram.
        bin_size: Size of each histogram bin.
        bin_start_curvature: Histogram bin start value.
        bin_end_curvature: Histogram bin end value.
        label_file: Label file to constrain statistics to a region.
        regional_percentages: Report integral percentages relative to the\
            region.
        high_pass_filter: High pass filter for curvature values.
        low_pass_filter: Low pass filter for curvature values.
        high_pass_filter_gaussian: High pass filter for Gaussian curvature\
            values.
        low_pass_filter_gaussian: Low pass filter for Gaussian curvature\
            values.
        filter_label: Store processed surface vertices in a label file.
        min_max_info: Output min/max information for the processed curvature.
        normalize_curvature: Normalize the curvature before computation.
        summary_condition: Write out stats as a summary condition.
        min_curvature_scale: Scale curvature values between min and max\
            curvature.
        max_curvature_scale: End value for curvature scaling.
        scale_factor: Scale curvature values with a factor.
        version: Print out version number.
        set_zero_vertex: Sets the curvature values at that index to zero.
        max_ulps: Toggle a more rigorous floating point comparison operation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisCurvatureStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_CURVATURE_STATS_METADATA)
    params = mris_curvature_stats_params(
        subject_name=subject_name,
        hemisphere=hemisphere,
        curvature_files=curvature_files,
        number_of_averages=number_of_averages,
        principal_curvatures=principal_curvatures,
        discrete_method=discrete_method,
        continuous_method=continuous_method,
        signed_principals=signed_principals,
        vertex_area_weigh=vertex_area_weigh,
        vertex_area_normalize=vertex_area_normalize,
        vertex_area_weigh_frac=vertex_area_weigh_frac,
        vertex_area_normalize_frac=vertex_area_normalize_frac,
        post_scale=post_scale,
        write_curvature_files=write_curvature_files,
        shape_index=shape_index,
        output_file_stem=output_file_stem,
        histogram_bins=histogram_bins,
        percentage_histogram_bins=percentage_histogram_bins,
        bin_size=bin_size,
        bin_start_curvature=bin_start_curvature,
        bin_end_curvature=bin_end_curvature,
        label_file=label_file,
        regional_percentages=regional_percentages,
        high_pass_filter=high_pass_filter,
        low_pass_filter=low_pass_filter,
        high_pass_filter_gaussian=high_pass_filter_gaussian,
        low_pass_filter_gaussian=low_pass_filter_gaussian,
        filter_label=filter_label,
        min_max_info=min_max_info,
        normalize_curvature=normalize_curvature,
        summary_condition=summary_condition,
        min_curvature_scale=min_curvature_scale,
        max_curvature_scale=max_curvature_scale,
        scale_factor=scale_factor,
        version=version,
        set_zero_vertex=set_zero_vertex,
        max_ulps=max_ulps,
    )
    return mris_curvature_stats_execute(params, execution)


__all__ = [
    "MRIS_CURVATURE_STATS_METADATA",
    "MrisCurvatureStatsOutputs",
    "MrisCurvatureStatsParameters",
    "mris_curvature_stats",
    "mris_curvature_stats_params",
]
