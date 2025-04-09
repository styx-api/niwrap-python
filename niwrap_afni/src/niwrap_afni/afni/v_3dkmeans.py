# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DKMEANS_METADATA = Metadata(
    id="75badc8d9b45ae3a536b3127bd2f907364fc748e.boutiques",
    name="3dkmeans",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dkmeansParameters = typing.TypedDict('V3dkmeansParameters', {
    "__STYX_TYPE__": typing.Literal["3dkmeans"],
    "version": bool,
    "input": list[InputPathType],
    "mask": typing.NotRequired[InputPathType | None],
    "mask_range": typing.NotRequired[list[float] | None],
    "cmask": typing.NotRequired[str | None],
    "jobname": typing.NotRequired[str | None],
    "prefix": typing.NotRequired[str | None],
    "distance_measure": typing.NotRequired[float | None],
    "num_clusters": typing.NotRequired[float | None],
    "remap_method": typing.NotRequired[str | None],
    "labeltable": typing.NotRequired[InputPathType | None],
    "clabels": typing.NotRequired[list[str] | None],
    "clust_init": typing.NotRequired[InputPathType | None],
    "num_repeats": typing.NotRequired[float | None],
    "rsigs": typing.NotRequired[InputPathType | None],
    "verbose": bool,
    "write_dists": bool,
    "voxdbg": typing.NotRequired[list[float] | None],
    "seed": typing.NotRequired[float | None],
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
        "3dkmeans": v_3dkmeans_cargs,
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
        "3dkmeans": v_3dkmeans_outputs,
    }.get(t)


class V3dkmeansOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dkmeans(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cluster_membership: OutputPathType | None
    """Output volume for the cluster membership."""
    cluster_distance: OutputPathType | None
    """Output volume for the cluster distance measures."""
    distances_text_file: OutputPathType
    """Output text file containing distances between clusters."""
    centroids_text_file: OutputPathType
    """Output text file containing cluster centroids."""
    within_cluster_sum_text_file: OutputPathType
    """Output text file containing within cluster sum of distances."""
    max_distance_text_file: OutputPathType
    """Output text file containing maximum distance within each cluster."""
    voxel_distance_to_centroid: OutputPathType
    """Output text file containing distance from voxel to its centroid."""


def v_3dkmeans_params(
    input_: list[InputPathType],
    version: bool = False,
    mask: InputPathType | None = None,
    mask_range: list[float] | None = None,
    cmask: str | None = None,
    jobname: str | None = None,
    prefix: str | None = None,
    distance_measure: float | None = None,
    num_clusters: float | None = None,
    remap_method: str | None = None,
    labeltable: InputPathType | None = None,
    clabels: list[str] | None = None,
    clust_init: InputPathType | None = None,
    num_repeats: float | None = None,
    rsigs: InputPathType | None = None,
    verbose: bool = False,
    write_dists: bool = False,
    voxdbg: list[float] | None = None,
    seed: float | None = None,
) -> V3dkmeansParameters:
    """
    Build parameters.
    
    Args:
        input_: Input data to be clustered. You can specify multiple filenames\
            in sequence and they will be concatenated internally.
        version:.
        mask: Dataset to be used as a mask; only voxels with nonzero values in\
            'mset' will be used.
        mask_range: Restrict the voxels from 'mset' to only those mask values\
            between 'a' and 'b' (inclusive).
        cmask: Execute the options enclosed in single quotes as a 3dcalc-like\
            program to produce a mask from the resulting 3D brick.
        jobname: Specify a different name for the output files. Default is\
            derived from the input file name.
        prefix: Specify a prefix for the output volumes. Default is the same as\
            jobname.
        distance_measure: Specifies distance measure for clustering. Supported\
            values: 0 (No clustering), 1 (Uncentered correlation distance), 2\
            (Pearson distance), 3 (Uncentered correlation distance, absolute\
            value), 4 (Pearson distance, absolute value), 5 (Spearman's rank\
            distance), 6 (Kendall's distance), 7 (Euclidean distance), 8\
            (City-block distance).
        num_clusters: Specify number of clusters.
        remap_method: Reassign clusters numbers based on METHOD: NONE\
            (default), COUNT, iCOUNT, MAG, iMAG.
        labeltable: Attach labeltable to clustering output.
        clabels: Provide a label for each cluster. Labels cannot start with\
            '-'.
        clust_init: Specify a dataset to initialize clustering. If provided,\
            sets -r 0.
        num_repeats: Number of times the k-means clustering algorithm is run.
        rsigs: Calculate distances from each voxel's signature to the\
            signatures in this multi-column file. No clustering done.
        verbose: Enable verbose mode.
        write_dists: Output text files containing various distance measures.
        voxdbg: Output debugging info for specified voxel (I J K).
        seed: Seed for the random number generator. Default is 1234567.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dkmeans",
        "version": version,
        "input": input_,
        "verbose": verbose,
        "write_dists": write_dists,
    }
    if mask is not None:
        params["mask"] = mask
    if mask_range is not None:
        params["mask_range"] = mask_range
    if cmask is not None:
        params["cmask"] = cmask
    if jobname is not None:
        params["jobname"] = jobname
    if prefix is not None:
        params["prefix"] = prefix
    if distance_measure is not None:
        params["distance_measure"] = distance_measure
    if num_clusters is not None:
        params["num_clusters"] = num_clusters
    if remap_method is not None:
        params["remap_method"] = remap_method
    if labeltable is not None:
        params["labeltable"] = labeltable
    if clabels is not None:
        params["clabels"] = clabels
    if clust_init is not None:
        params["clust_init"] = clust_init
    if num_repeats is not None:
        params["num_repeats"] = num_repeats
    if rsigs is not None:
        params["rsigs"] = rsigs
    if voxdbg is not None:
        params["voxdbg"] = voxdbg
    if seed is not None:
        params["seed"] = seed
    return params


def v_3dkmeans_cargs(
    params: V3dkmeansParameters,
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
    cargs.append("3dkmeans")
    if params.get("version"):
        cargs.append("--version")
    cargs.extend([
        "-f",
        *[execution.input_file(f) for f in params.get("input")]
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("mask_range") is not None:
        cargs.extend([
            "-mrange",
            *map(str, params.get("mask_range"))
        ])
    if params.get("cmask") is not None:
        cargs.extend([
            "-cmask",
            params.get("cmask")
        ])
    if params.get("jobname") is not None:
        cargs.extend([
            "-u",
            params.get("jobname")
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("distance_measure") is not None:
        cargs.extend([
            "-g",
            str(params.get("distance_measure"))
        ])
    if params.get("num_clusters") is not None:
        cargs.extend([
            "-k",
            str(params.get("num_clusters"))
        ])
    if params.get("remap_method") is not None:
        cargs.extend([
            "-remap",
            params.get("remap_method")
        ])
    if params.get("labeltable") is not None:
        cargs.extend([
            "-labeltable",
            execution.input_file(params.get("labeltable"))
        ])
    if params.get("clabels") is not None:
        cargs.extend([
            "-clabels",
            *params.get("clabels")
        ])
    if params.get("clust_init") is not None:
        cargs.extend([
            "-clust_init",
            execution.input_file(params.get("clust_init"))
        ])
    if params.get("num_repeats") is not None:
        cargs.extend([
            "-r",
            str(params.get("num_repeats"))
        ])
    if params.get("rsigs") is not None:
        cargs.extend([
            "-rsigs",
            execution.input_file(params.get("rsigs"))
        ])
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("write_dists"):
        cargs.append("-write_dists")
    if params.get("voxdbg") is not None:
        cargs.extend([
            "-voxdbg",
            *map(str, params.get("voxdbg"))
        ])
    if params.get("seed") is not None:
        cargs.extend([
            "-seed",
            str(params.get("seed"))
        ])
    return cargs


def v_3dkmeans_outputs(
    params: V3dkmeansParameters,
    execution: Execution,
) -> V3dkmeansOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dkmeansOutputs(
        root=execution.output_file("."),
        cluster_membership=execution.output_file(params.get("jobname") + "_membership.nii.gz") if (params.get("jobname") is not None) else None,
        cluster_distance=execution.output_file(params.get("jobname") + "_distance.nii.gz") if (params.get("jobname") is not None) else None,
        distances_text_file=execution.output_file("FILE.dis.1D"),
        centroids_text_file=execution.output_file("FILE.cen.1D"),
        within_cluster_sum_text_file=execution.output_file("FILE.info1.1D"),
        max_distance_text_file=execution.output_file("FILE.info2.1D"),
        voxel_distance_to_centroid=execution.output_file("FILE.vcd.1D"),
    )
    return ret


def v_3dkmeans_execute(
    params: V3dkmeansParameters,
    execution: Execution,
) -> V3dkmeansOutputs:
    """
    3d+t Clustering segmentation based on The C clustering library.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dkmeansOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dkmeans_cargs(params, execution)
    ret = v_3dkmeans_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dkmeans(
    input_: list[InputPathType],
    version: bool = False,
    mask: InputPathType | None = None,
    mask_range: list[float] | None = None,
    cmask: str | None = None,
    jobname: str | None = None,
    prefix: str | None = None,
    distance_measure: float | None = None,
    num_clusters: float | None = None,
    remap_method: str | None = None,
    labeltable: InputPathType | None = None,
    clabels: list[str] | None = None,
    clust_init: InputPathType | None = None,
    num_repeats: float | None = None,
    rsigs: InputPathType | None = None,
    verbose: bool = False,
    write_dists: bool = False,
    voxdbg: list[float] | None = None,
    seed: float | None = None,
    runner: Runner | None = None,
) -> V3dkmeansOutputs:
    """
    3d+t Clustering segmentation based on The C clustering library.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_: Input data to be clustered. You can specify multiple filenames\
            in sequence and they will be concatenated internally.
        version:.
        mask: Dataset to be used as a mask; only voxels with nonzero values in\
            'mset' will be used.
        mask_range: Restrict the voxels from 'mset' to only those mask values\
            between 'a' and 'b' (inclusive).
        cmask: Execute the options enclosed in single quotes as a 3dcalc-like\
            program to produce a mask from the resulting 3D brick.
        jobname: Specify a different name for the output files. Default is\
            derived from the input file name.
        prefix: Specify a prefix for the output volumes. Default is the same as\
            jobname.
        distance_measure: Specifies distance measure for clustering. Supported\
            values: 0 (No clustering), 1 (Uncentered correlation distance), 2\
            (Pearson distance), 3 (Uncentered correlation distance, absolute\
            value), 4 (Pearson distance, absolute value), 5 (Spearman's rank\
            distance), 6 (Kendall's distance), 7 (Euclidean distance), 8\
            (City-block distance).
        num_clusters: Specify number of clusters.
        remap_method: Reassign clusters numbers based on METHOD: NONE\
            (default), COUNT, iCOUNT, MAG, iMAG.
        labeltable: Attach labeltable to clustering output.
        clabels: Provide a label for each cluster. Labels cannot start with\
            '-'.
        clust_init: Specify a dataset to initialize clustering. If provided,\
            sets -r 0.
        num_repeats: Number of times the k-means clustering algorithm is run.
        rsigs: Calculate distances from each voxel's signature to the\
            signatures in this multi-column file. No clustering done.
        verbose: Enable verbose mode.
        write_dists: Output text files containing various distance measures.
        voxdbg: Output debugging info for specified voxel (I J K).
        seed: Seed for the random number generator. Default is 1234567.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dkmeansOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DKMEANS_METADATA)
    params = v_3dkmeans_params(
        version=version,
        input_=input_,
        mask=mask,
        mask_range=mask_range,
        cmask=cmask,
        jobname=jobname,
        prefix=prefix,
        distance_measure=distance_measure,
        num_clusters=num_clusters,
        remap_method=remap_method,
        labeltable=labeltable,
        clabels=clabels,
        clust_init=clust_init,
        num_repeats=num_repeats,
        rsigs=rsigs,
        verbose=verbose,
        write_dists=write_dists,
        voxdbg=voxdbg,
        seed=seed,
    )
    return v_3dkmeans_execute(params, execution)


__all__ = [
    "V3dkmeansOutputs",
    "V3dkmeansParameters",
    "V_3DKMEANS_METADATA",
    "v_3dkmeans",
    "v_3dkmeans_params",
]
