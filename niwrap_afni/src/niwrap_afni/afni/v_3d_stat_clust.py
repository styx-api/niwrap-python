# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_STAT_CLUST_METADATA = Metadata(
    id="284f4ab8bc45b6b47b8622cab065942bd38efb9a.boutiques",
    name="3dStatClust",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dStatClustParameters = typing.TypedDict('V3dStatClustParameters', {
    "__STYX_TYPE__": typing.Literal["3dStatClust"],
    "prefix": typing.NotRequired[str | None],
    "session_dir": typing.NotRequired[str | None],
    "verbose": bool,
    "dist_euc": bool,
    "dist_ind": bool,
    "dist_cor": bool,
    "thresh": str,
    "nclust": float,
    "datasets": list[str],
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
        "3dStatClust": v_3d_stat_clust_cargs,
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
        "3dStatClust": v_3d_stat_clust_outputs,
    }.get(t)


class V3dStatClustOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_stat_clust(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_head: OutputPathType | None
    """Output dataset header"""
    output_brick: OutputPathType | None
    """Output dataset brick"""


def v_3d_stat_clust_params(
    thresh: str,
    nclust: float,
    datasets: list[str],
    prefix: str | None = None,
    session_dir: str | None = None,
    verbose: bool = False,
    dist_euc: bool = False,
    dist_ind: bool = False,
    dist_cor: bool = False,
) -> V3dStatClustParameters:
    """
    Build parameters.
    
    Args:
        thresh: Threshold statistic from file tname. Only voxels whose\
            threshold statistic is greater than t in absolute value will be\
            considered. If file tname contains more than 1 sub-brick, the threshold\
            stat. sub-brick must be specified.
        nclust: Maximum number of clusters for output (= number of sub-bricks\
            in output dataset).
        datasets: Parameter datasets.
        prefix: Use 'pname' for the output dataset prefix name.
        session_dir: Use 'dir' for the output dataset session directory.
        verbose: Print out verbose output as the program proceeds.
        dist_euc: Calculate Euclidean distance between parameters.
        dist_ind: Statistical distance for independent parameters.
        dist_cor: Statistical distance for correlated parameters.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dStatClust",
        "verbose": verbose,
        "dist_euc": dist_euc,
        "dist_ind": dist_ind,
        "dist_cor": dist_cor,
        "thresh": thresh,
        "nclust": nclust,
        "datasets": datasets,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if session_dir is not None:
        params["session_dir"] = session_dir
    return params


def v_3d_stat_clust_cargs(
    params: V3dStatClustParameters,
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
    cargs.append("3dStatClust")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("session_dir") is not None:
        cargs.extend([
            "-session",
            params.get("session_dir")
        ])
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("dist_euc"):
        cargs.append("-dist_euc")
    if params.get("dist_ind"):
        cargs.append("-dist_ind")
    if params.get("dist_cor"):
        cargs.append("-dist_cor")
    cargs.extend([
        "-thresh",
        params.get("thresh")
    ])
    cargs.extend([
        "-nclust",
        str(params.get("nclust"))
    ])
    cargs.extend(params.get("datasets"))
    return cargs


def v_3d_stat_clust_outputs(
    params: V3dStatClustParameters,
    execution: Execution,
) -> V3dStatClustOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dStatClustOutputs(
        root=execution.output_file("."),
        output_head=execution.output_file(params.get("prefix") + "+orig.HEAD") if (params.get("prefix") is not None) else None,
        output_brick=execution.output_file(params.get("prefix") + "+orig.BRIK") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_stat_clust_execute(
    params: V3dStatClustParameters,
    execution: Execution,
) -> V3dStatClustOutputs:
    """
    Perform agglomerative hierarchical clustering for user specified parameter
    sub-bricks, for all voxels whose threshold statistic is above a user specified
    value.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dStatClustOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_stat_clust_cargs(params, execution)
    ret = v_3d_stat_clust_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_stat_clust(
    thresh: str,
    nclust: float,
    datasets: list[str],
    prefix: str | None = None,
    session_dir: str | None = None,
    verbose: bool = False,
    dist_euc: bool = False,
    dist_ind: bool = False,
    dist_cor: bool = False,
    runner: Runner | None = None,
) -> V3dStatClustOutputs:
    """
    Perform agglomerative hierarchical clustering for user specified parameter
    sub-bricks, for all voxels whose threshold statistic is above a user specified
    value.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        thresh: Threshold statistic from file tname. Only voxels whose\
            threshold statistic is greater than t in absolute value will be\
            considered. If file tname contains more than 1 sub-brick, the threshold\
            stat. sub-brick must be specified.
        nclust: Maximum number of clusters for output (= number of sub-bricks\
            in output dataset).
        datasets: Parameter datasets.
        prefix: Use 'pname' for the output dataset prefix name.
        session_dir: Use 'dir' for the output dataset session directory.
        verbose: Print out verbose output as the program proceeds.
        dist_euc: Calculate Euclidean distance between parameters.
        dist_ind: Statistical distance for independent parameters.
        dist_cor: Statistical distance for correlated parameters.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dStatClustOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_STAT_CLUST_METADATA)
    params = v_3d_stat_clust_params(
        prefix=prefix,
        session_dir=session_dir,
        verbose=verbose,
        dist_euc=dist_euc,
        dist_ind=dist_ind,
        dist_cor=dist_cor,
        thresh=thresh,
        nclust=nclust,
        datasets=datasets,
    )
    return v_3d_stat_clust_execute(params, execution)


__all__ = [
    "V3dStatClustOutputs",
    "V3dStatClustParameters",
    "V_3D_STAT_CLUST_METADATA",
    "v_3d_stat_clust",
    "v_3d_stat_clust_params",
]
