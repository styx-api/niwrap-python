# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CLUSTER_METADATA = Metadata(
    id="dc6e00e2143aabe03722abc3629250d0dce2e99d.boutiques",
    name="cluster",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


ClusterParameters = typing.TypedDict('ClusterParameters', {
    "__STYXTYPE__": typing.Literal["cluster"],
    "connectivity": typing.NotRequired[int | None],
    "cope_file": typing.NotRequired[InputPathType | None],
    "dlh": typing.NotRequired[float | None],
    "find_min": bool,
    "fractional": bool,
    "in_file": InputPathType,
    "minclustersize": bool,
    "no_table": bool,
    "num_maxima": typing.NotRequired[int | None],
    "out_index_file": str,
    "out_index_file_2": typing.NotRequired[InputPathType | None],
    "out_localmax_txt_file": str,
    "out_localmax_txt_file_2": typing.NotRequired[InputPathType | None],
    "out_localmax_vol_file": str,
    "out_localmax_vol_file_2": typing.NotRequired[InputPathType | None],
    "out_max_file": str,
    "out_max_file_2": typing.NotRequired[InputPathType | None],
    "out_mean_file": str,
    "out_mean_file_2": typing.NotRequired[InputPathType | None],
    "out_pval_file": str,
    "out_pval_file_2": typing.NotRequired[InputPathType | None],
    "out_size_file": str,
    "out_size_file_2": typing.NotRequired[InputPathType | None],
    "out_threshold_file": str,
    "out_threshold_file_2": typing.NotRequired[InputPathType | None],
    "output_type": typing.NotRequired[typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None],
    "peak_distance": typing.NotRequired[float | None],
    "pthreshold": typing.NotRequired[float | None],
    "std_space_file": typing.NotRequired[InputPathType | None],
    "threshold": float,
    "use_mm": bool,
    "volume": typing.NotRequired[int | None],
    "warpfield_file": typing.NotRequired[InputPathType | None],
    "xfm_file": typing.NotRequired[InputPathType | None],
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
        "cluster": cluster_cargs,
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
        "cluster": cluster_outputs,
    }.get(t)


class ClusterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cluster(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    index_file: OutputPathType
    """Output of cluster index (in size order)."""
    localmax_txt_file: OutputPathType
    """Local maxima text file."""
    localmax_vol_file: OutputPathType
    """Output of local maxima volume."""
    max_file: OutputPathType
    """Filename for output of max image."""
    mean_file: OutputPathType
    """Filename for output of mean image."""
    pval_file: OutputPathType
    """Filename for image output of log pvals."""
    size_file: OutputPathType
    """Filename for output of size image."""
    threshold_file: OutputPathType
    """Thresholded image."""


def cluster_params(
    in_file: InputPathType,
    out_index_file: str,
    out_localmax_txt_file: str,
    out_localmax_vol_file: str,
    out_max_file: str,
    out_mean_file: str,
    out_pval_file: str,
    out_size_file: str,
    out_threshold_file: str,
    threshold: float,
    connectivity: int | None = None,
    cope_file: InputPathType | None = None,
    dlh: float | None = None,
    find_min: bool = False,
    fractional: bool = False,
    minclustersize: bool = False,
    no_table: bool = False,
    num_maxima: int | None = None,
    out_index_file_2: InputPathType | None = None,
    out_localmax_txt_file_2: InputPathType | None = None,
    out_localmax_vol_file_2: InputPathType | None = None,
    out_max_file_2: InputPathType | None = None,
    out_mean_file_2: InputPathType | None = None,
    out_pval_file_2: InputPathType | None = None,
    out_size_file_2: InputPathType | None = None,
    out_threshold_file_2: InputPathType | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    peak_distance: float | None = None,
    pthreshold: float | None = None,
    std_space_file: InputPathType | None = None,
    use_mm: bool = False,
    volume: int | None = None,
    warpfield_file: InputPathType | None = None,
    xfm_file: InputPathType | None = None,
) -> ClusterParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input volume.
        out_index_file: A boolean or file. Output of cluster index (in size\
            order).
        out_localmax_txt_file: A boolean or file. Local maxima text file.
        out_localmax_vol_file: A boolean or file. Output of local maxima\
            volume.
        out_max_file: A boolean or file. Filename for output of max image.
        out_mean_file: A boolean or file. Filename for output of mean image.
        out_pval_file: A boolean or file. Filename for image output of log\
            pvals.
        out_size_file: A boolean or file. Filename for output of size image.
        out_threshold_file: A boolean or file. Thresholded image.
        threshold: Threshold for input volume.
        connectivity: The connectivity of voxels (default 26).
        cope_file: Cope volume.
        dlh: Smoothness estimate = sqrt(det(lambda)).
        find_min: Find minima instead of maxima.
        fractional: Interprets the threshold as a fraction of the robust range.
        minclustersize: Prints out minimum significant cluster size.
        no_table: Suppresses printing of the table info.
        num_maxima: No of local maxima to report.
        out_index_file_2: A boolean or file. Output of cluster index (in size\
            order).
        out_localmax_txt_file_2: A boolean or file. Local maxima text file.
        out_localmax_vol_file_2: A boolean or file. Output of local maxima\
            volume.
        out_max_file_2: A boolean or file. Filename for output of max image.
        out_mean_file_2: A boolean or file. Filename for output of mean image.
        out_pval_file_2: A boolean or file. Filename for image output of log\
            pvals.
        out_size_file_2: A boolean or file. Filename for output of size image.
        out_threshold_file_2: A boolean or file. Thresholded image.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        peak_distance: Minimum distance between local maxima/minima, in mm\
            (default 0).
        pthreshold: P-threshold for clusters.
        std_space_file: Filename for standard-space volume.
        use_mm: Use mm, not voxel, coordinates.
        volume: Number of voxels in the mask.
        warpfield_file: File containing warpfield.
        xfm_file: Filename for linear: input->standard-space transform.\
            non-linear: input->highres transform.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cluster",
        "find_min": find_min,
        "fractional": fractional,
        "in_file": in_file,
        "minclustersize": minclustersize,
        "no_table": no_table,
        "out_index_file": out_index_file,
        "out_localmax_txt_file": out_localmax_txt_file,
        "out_localmax_vol_file": out_localmax_vol_file,
        "out_max_file": out_max_file,
        "out_mean_file": out_mean_file,
        "out_pval_file": out_pval_file,
        "out_size_file": out_size_file,
        "out_threshold_file": out_threshold_file,
        "threshold": threshold,
        "use_mm": use_mm,
    }
    if connectivity is not None:
        params["connectivity"] = connectivity
    if cope_file is not None:
        params["cope_file"] = cope_file
    if dlh is not None:
        params["dlh"] = dlh
    if num_maxima is not None:
        params["num_maxima"] = num_maxima
    if out_index_file_2 is not None:
        params["out_index_file_2"] = out_index_file_2
    if out_localmax_txt_file_2 is not None:
        params["out_localmax_txt_file_2"] = out_localmax_txt_file_2
    if out_localmax_vol_file_2 is not None:
        params["out_localmax_vol_file_2"] = out_localmax_vol_file_2
    if out_max_file_2 is not None:
        params["out_max_file_2"] = out_max_file_2
    if out_mean_file_2 is not None:
        params["out_mean_file_2"] = out_mean_file_2
    if out_pval_file_2 is not None:
        params["out_pval_file_2"] = out_pval_file_2
    if out_size_file_2 is not None:
        params["out_size_file_2"] = out_size_file_2
    if out_threshold_file_2 is not None:
        params["out_threshold_file_2"] = out_threshold_file_2
    if output_type is not None:
        params["output_type"] = output_type
    if peak_distance is not None:
        params["peak_distance"] = peak_distance
    if pthreshold is not None:
        params["pthreshold"] = pthreshold
    if std_space_file is not None:
        params["std_space_file"] = std_space_file
    if volume is not None:
        params["volume"] = volume
    if warpfield_file is not None:
        params["warpfield_file"] = warpfield_file
    if xfm_file is not None:
        params["xfm_file"] = xfm_file
    return params


def cluster_cargs(
    params: ClusterParameters,
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
    cargs.append("cluster")
    if params.get("connectivity") is not None:
        cargs.append("--connectivity=" + str(params.get("connectivity")))
    if params.get("cope_file") is not None:
        cargs.append("--cope=" + execution.input_file(params.get("cope_file")))
    if params.get("dlh") is not None:
        cargs.append("--dlh=" + str(params.get("dlh")))
    if params.get("find_min"):
        cargs.append("--min")
    if params.get("fractional"):
        cargs.append("--fractional")
    cargs.append("--in=" + execution.input_file(params.get("in_file")))
    if params.get("minclustersize"):
        cargs.append("--minclustersize")
    if params.get("no_table"):
        cargs.append("--no_table")
    if params.get("num_maxima") is not None:
        cargs.append("--num=" + str(params.get("num_maxima")))
    cargs.append("--oindex=" + params.get("out_index_file"))
    if params.get("out_index_file_2") is not None:
        cargs.append("--oindex=" + execution.input_file(params.get("out_index_file_2")))
    cargs.append("--olmax=" + params.get("out_localmax_txt_file"))
    if params.get("out_localmax_txt_file_2") is not None:
        cargs.append("--olmax=" + execution.input_file(params.get("out_localmax_txt_file_2")))
    cargs.append("--olmaxim=" + params.get("out_localmax_vol_file"))
    if params.get("out_localmax_vol_file_2") is not None:
        cargs.append("--olmaxim=" + execution.input_file(params.get("out_localmax_vol_file_2")))
    cargs.append("--omax=" + params.get("out_max_file"))
    if params.get("out_max_file_2") is not None:
        cargs.append("--omax=" + execution.input_file(params.get("out_max_file_2")))
    cargs.append("--omean=" + params.get("out_mean_file"))
    if params.get("out_mean_file_2") is not None:
        cargs.append("--omean=" + execution.input_file(params.get("out_mean_file_2")))
    cargs.append("--opvals=" + params.get("out_pval_file"))
    if params.get("out_pval_file_2") is not None:
        cargs.append("--opvals=" + execution.input_file(params.get("out_pval_file_2")))
    cargs.append("--osize=" + params.get("out_size_file"))
    if params.get("out_size_file_2") is not None:
        cargs.append("--osize=" + execution.input_file(params.get("out_size_file_2")))
    cargs.append("--othresh=" + params.get("out_threshold_file"))
    if params.get("out_threshold_file_2") is not None:
        cargs.append("--othresh=" + execution.input_file(params.get("out_threshold_file_2")))
    if params.get("output_type") is not None:
        cargs.append(params.get("output_type"))
    if params.get("peak_distance") is not None:
        cargs.append("--peakdist=" + str(params.get("peak_distance")))
    if params.get("pthreshold") is not None:
        cargs.append("--pthresh=" + str(params.get("pthreshold")))
    if params.get("std_space_file") is not None:
        cargs.append("--stdvol=" + execution.input_file(params.get("std_space_file")))
    cargs.append("--thresh=" + str(params.get("threshold")))
    if params.get("use_mm"):
        cargs.append("--mm")
    if params.get("volume") is not None:
        cargs.append("--volume=" + str(params.get("volume")))
    if params.get("warpfield_file") is not None:
        cargs.append("--warpvol=" + execution.input_file(params.get("warpfield_file")))
    if params.get("xfm_file") is not None:
        cargs.append("--xfm=" + execution.input_file(params.get("xfm_file")))
    return cargs


def cluster_outputs(
    params: ClusterParameters,
    execution: Execution,
) -> ClusterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ClusterOutputs(
        root=execution.output_file("."),
        index_file=execution.output_file("index_file"),
        localmax_txt_file=execution.output_file("localmax_txt_file"),
        localmax_vol_file=execution.output_file("localmax_vol_file"),
        max_file=execution.output_file("max_file"),
        mean_file=execution.output_file("mean_file"),
        pval_file=execution.output_file("pval_file"),
        size_file=execution.output_file("size_file"),
        threshold_file=execution.output_file("threshold_file"),
    )
    return ret


def cluster_execute(
    params: ClusterParameters,
    execution: Execution,
) -> ClusterOutputs:
    """
    Uses FSL cluster to perform clustering on statistical output.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ClusterOutputs`).
    """
    params = execution.params(params)
    cargs = cluster_cargs(params, execution)
    ret = cluster_outputs(params, execution)
    execution.run(cargs)
    return ret


def cluster(
    in_file: InputPathType,
    out_index_file: str,
    out_localmax_txt_file: str,
    out_localmax_vol_file: str,
    out_max_file: str,
    out_mean_file: str,
    out_pval_file: str,
    out_size_file: str,
    out_threshold_file: str,
    threshold: float,
    connectivity: int | None = None,
    cope_file: InputPathType | None = None,
    dlh: float | None = None,
    find_min: bool = False,
    fractional: bool = False,
    minclustersize: bool = False,
    no_table: bool = False,
    num_maxima: int | None = None,
    out_index_file_2: InputPathType | None = None,
    out_localmax_txt_file_2: InputPathType | None = None,
    out_localmax_vol_file_2: InputPathType | None = None,
    out_max_file_2: InputPathType | None = None,
    out_mean_file_2: InputPathType | None = None,
    out_pval_file_2: InputPathType | None = None,
    out_size_file_2: InputPathType | None = None,
    out_threshold_file_2: InputPathType | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    peak_distance: float | None = None,
    pthreshold: float | None = None,
    std_space_file: InputPathType | None = None,
    use_mm: bool = False,
    volume: int | None = None,
    warpfield_file: InputPathType | None = None,
    xfm_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> ClusterOutputs:
    """
    Uses FSL cluster to perform clustering on statistical output.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_file: Input volume.
        out_index_file: A boolean or file. Output of cluster index (in size\
            order).
        out_localmax_txt_file: A boolean or file. Local maxima text file.
        out_localmax_vol_file: A boolean or file. Output of local maxima\
            volume.
        out_max_file: A boolean or file. Filename for output of max image.
        out_mean_file: A boolean or file. Filename for output of mean image.
        out_pval_file: A boolean or file. Filename for image output of log\
            pvals.
        out_size_file: A boolean or file. Filename for output of size image.
        out_threshold_file: A boolean or file. Thresholded image.
        threshold: Threshold for input volume.
        connectivity: The connectivity of voxels (default 26).
        cope_file: Cope volume.
        dlh: Smoothness estimate = sqrt(det(lambda)).
        find_min: Find minima instead of maxima.
        fractional: Interprets the threshold as a fraction of the robust range.
        minclustersize: Prints out minimum significant cluster size.
        no_table: Suppresses printing of the table info.
        num_maxima: No of local maxima to report.
        out_index_file_2: A boolean or file. Output of cluster index (in size\
            order).
        out_localmax_txt_file_2: A boolean or file. Local maxima text file.
        out_localmax_vol_file_2: A boolean or file. Output of local maxima\
            volume.
        out_max_file_2: A boolean or file. Filename for output of max image.
        out_mean_file_2: A boolean or file. Filename for output of mean image.
        out_pval_file_2: A boolean or file. Filename for image output of log\
            pvals.
        out_size_file_2: A boolean or file. Filename for output of size image.
        out_threshold_file_2: A boolean or file. Thresholded image.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        peak_distance: Minimum distance between local maxima/minima, in mm\
            (default 0).
        pthreshold: P-threshold for clusters.
        std_space_file: Filename for standard-space volume.
        use_mm: Use mm, not voxel, coordinates.
        volume: Number of voxels in the mask.
        warpfield_file: File containing warpfield.
        xfm_file: Filename for linear: input->standard-space transform.\
            non-linear: input->highres transform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ClusterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CLUSTER_METADATA)
    params = cluster_params(
        connectivity=connectivity,
        cope_file=cope_file,
        dlh=dlh,
        find_min=find_min,
        fractional=fractional,
        in_file=in_file,
        minclustersize=minclustersize,
        no_table=no_table,
        num_maxima=num_maxima,
        out_index_file=out_index_file,
        out_index_file_2=out_index_file_2,
        out_localmax_txt_file=out_localmax_txt_file,
        out_localmax_txt_file_2=out_localmax_txt_file_2,
        out_localmax_vol_file=out_localmax_vol_file,
        out_localmax_vol_file_2=out_localmax_vol_file_2,
        out_max_file=out_max_file,
        out_max_file_2=out_max_file_2,
        out_mean_file=out_mean_file,
        out_mean_file_2=out_mean_file_2,
        out_pval_file=out_pval_file,
        out_pval_file_2=out_pval_file_2,
        out_size_file=out_size_file,
        out_size_file_2=out_size_file_2,
        out_threshold_file=out_threshold_file,
        out_threshold_file_2=out_threshold_file_2,
        output_type=output_type,
        peak_distance=peak_distance,
        pthreshold=pthreshold,
        std_space_file=std_space_file,
        threshold=threshold,
        use_mm=use_mm,
        volume=volume,
        warpfield_file=warpfield_file,
        xfm_file=xfm_file,
    )
    return cluster_execute(params, execution)


__all__ = [
    "CLUSTER_METADATA",
    "ClusterOutputs",
    "ClusterParameters",
    "cluster",
    "cluster_params",
]
