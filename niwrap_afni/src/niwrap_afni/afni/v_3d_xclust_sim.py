# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_XCLUST_SIM_METADATA = Metadata(
    id="da8dfc6fd73a07401ddf1667768a4f16b84acebc.boutiques",
    name="3dXClustSim",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dXclustSimParameters = typing.TypedDict('V3dXclustSimParameters', {
    "__STYX_TYPE__": typing.Literal["3dXClustSim"],
    "inset": InputPathType,
    "insdat": typing.NotRequired[InputPathType | None],
    "nn": typing.NotRequired[float | None],
    "sid": typing.NotRequired[float | None],
    "hpow": typing.NotRequired[list[float] | None],
    "ncase": typing.NotRequired[list[str] | None],
    "pthr": typing.NotRequired[list[float] | None],
    "fpr": typing.NotRequired[float | None],
    "multiFPR": bool,
    "minclust": typing.NotRequired[float | None],
    "local": bool,
    "global": bool,
    "nolocal": bool,
    "noglobal": bool,
    "splitfrac": typing.NotRequired[float | None],
    "prefix": typing.NotRequired[str | None],
    "verbose": bool,
    "quiet": bool,
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
        "3dXClustSim": v_3d_xclust_sim_cargs,
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
        "3dXClustSim": v_3d_xclust_sim_outputs,
    }.get(t)


class V3dXclustSimOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_xclust_sim(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_mthresh: OutputPathType | None
    """Output multi-threshold files for each -ncase input"""


def v_3d_xclust_sim_params(
    inset: InputPathType,
    insdat: InputPathType | None = None,
    nn: float | None = None,
    sid: float | None = None,
    hpow: list[float] | None = None,
    ncase: list[str] | None = None,
    pthr: list[float] | None = None,
    fpr: float | None = None,
    multi_fpr: bool = False,
    minclust: float | None = None,
    local: bool = False,
    global_: bool = False,
    nolocal: bool = False,
    noglobal: bool = False,
    splitfrac: float | None = None,
    prefix: str | None = None,
    verbose: bool = False,
    quiet: bool = False,
) -> V3dXclustSimParameters:
    """
    Build parameters.
    
    Args:
        inset: Mask sdata file (from 3dtoXdataset or 3dttest++).
        insdat: Data files in the '.sdat' format.
        nn: Neighborhood connectivity (1, 2, or 3). Default is 2.
        sid: Sidedness: 1 (one-sided) or 2 (two-sided). Default is 2.
        hpow: H power values (can be a subset of 0, 1, 2). Default is 2.
        ncase: Number of cases with labels. Default is 1 A.
        pthr: List of p-value thresholds. Default is 0.0100 0.0056 0.0031\
            0.0018 0.0010.
        fpr: Set global FPR goal to an integer ff between 2 and 9. Default is\
            5.
        multi_fpr: Compute results for multiple FPR goals (2%, 3%, ... 9%).
        minclust: Minimum cluster size in voxels. Default is 5.
        local: Do voxel-wise (local) ETAC computations.
        global_: Do volume-wise (global) ETAC computations.
        nolocal: Do not perform voxel-wise ETAC computations.
        noglobal: Do not perform volume-wise ETAC computations.
        splitfrac: Fraction to split simulations into pieces (0.2 < F < 0.8).
        prefix: Output filename prefix.
        verbose: Be more verbose.
        quiet: Silent mode.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dXClustSim",
        "inset": inset,
        "multiFPR": multi_fpr,
        "local": local,
        "global": global_,
        "nolocal": nolocal,
        "noglobal": noglobal,
        "verbose": verbose,
        "quiet": quiet,
    }
    if insdat is not None:
        params["insdat"] = insdat
    if nn is not None:
        params["nn"] = nn
    if sid is not None:
        params["sid"] = sid
    if hpow is not None:
        params["hpow"] = hpow
    if ncase is not None:
        params["ncase"] = ncase
    if pthr is not None:
        params["pthr"] = pthr
    if fpr is not None:
        params["fpr"] = fpr
    if minclust is not None:
        params["minclust"] = minclust
    if splitfrac is not None:
        params["splitfrac"] = splitfrac
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_xclust_sim_cargs(
    params: V3dXclustSimParameters,
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
    cargs.append("3dXClustSim")
    cargs.append(execution.input_file(params.get("inset")))
    if params.get("insdat") is not None:
        cargs.append(execution.input_file(params.get("insdat")))
    if params.get("nn") is not None:
        cargs.extend([
            "-NN",
            str(params.get("nn"))
        ])
    if params.get("sid") is not None:
        cargs.extend([
            "-sid",
            str(params.get("sid"))
        ])
    if params.get("hpow") is not None:
        cargs.extend([
            "-hpow",
            *map(str, params.get("hpow"))
        ])
    if params.get("ncase") is not None:
        cargs.extend([
            "-ncase",
            *params.get("ncase")
        ])
    if params.get("pthr") is not None:
        cargs.extend([
            "-pthr",
            *map(str, params.get("pthr"))
        ])
    if params.get("fpr") is not None:
        cargs.extend([
            "-FPR",
            str(params.get("fpr"))
        ])
    if params.get("multiFPR"):
        cargs.append("-multiFPR")
    if params.get("minclust") is not None:
        cargs.extend([
            "-minclust",
            str(params.get("minclust"))
        ])
    if params.get("local"):
        cargs.append("-local")
    if params.get("global"):
        cargs.append("-global")
    if params.get("nolocal"):
        cargs.append("-nolocal")
    if params.get("noglobal"):
        cargs.append("-noglobal")
    if params.get("splitfrac") is not None:
        cargs.extend([
            "-splitfrac",
            str(params.get("splitfrac"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("quiet"):
        cargs.append("-quiet")
    return cargs


def v_3d_xclust_sim_outputs(
    params: V3dXclustSimParameters,
    execution: Execution,
) -> V3dXclustSimOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dXclustSimOutputs(
        root=execution.output_file("."),
        out_mthresh=execution.output_file(params.get("prefix") + ".mthresh.*.nii") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_xclust_sim_execute(
    params: V3dXclustSimParameters,
    execution: Execution,
) -> V3dXclustSimOutputs:
    """
    ETAC processing tool to find cluster figure of merit (FOM) thresholds.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dXclustSimOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_xclust_sim_cargs(params, execution)
    ret = v_3d_xclust_sim_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_xclust_sim(
    inset: InputPathType,
    insdat: InputPathType | None = None,
    nn: float | None = None,
    sid: float | None = None,
    hpow: list[float] | None = None,
    ncase: list[str] | None = None,
    pthr: list[float] | None = None,
    fpr: float | None = None,
    multi_fpr: bool = False,
    minclust: float | None = None,
    local: bool = False,
    global_: bool = False,
    nolocal: bool = False,
    noglobal: bool = False,
    splitfrac: float | None = None,
    prefix: str | None = None,
    verbose: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dXclustSimOutputs:
    """
    ETAC processing tool to find cluster figure of merit (FOM) thresholds.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        inset: Mask sdata file (from 3dtoXdataset or 3dttest++).
        insdat: Data files in the '.sdat' format.
        nn: Neighborhood connectivity (1, 2, or 3). Default is 2.
        sid: Sidedness: 1 (one-sided) or 2 (two-sided). Default is 2.
        hpow: H power values (can be a subset of 0, 1, 2). Default is 2.
        ncase: Number of cases with labels. Default is 1 A.
        pthr: List of p-value thresholds. Default is 0.0100 0.0056 0.0031\
            0.0018 0.0010.
        fpr: Set global FPR goal to an integer ff between 2 and 9. Default is\
            5.
        multi_fpr: Compute results for multiple FPR goals (2%, 3%, ... 9%).
        minclust: Minimum cluster size in voxels. Default is 5.
        local: Do voxel-wise (local) ETAC computations.
        global_: Do volume-wise (global) ETAC computations.
        nolocal: Do not perform voxel-wise ETAC computations.
        noglobal: Do not perform volume-wise ETAC computations.
        splitfrac: Fraction to split simulations into pieces (0.2 < F < 0.8).
        prefix: Output filename prefix.
        verbose: Be more verbose.
        quiet: Silent mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dXclustSimOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_XCLUST_SIM_METADATA)
    params = v_3d_xclust_sim_params(
        inset=inset,
        insdat=insdat,
        nn=nn,
        sid=sid,
        hpow=hpow,
        ncase=ncase,
        pthr=pthr,
        fpr=fpr,
        multi_fpr=multi_fpr,
        minclust=minclust,
        local=local,
        global_=global_,
        nolocal=nolocal,
        noglobal=noglobal,
        splitfrac=splitfrac,
        prefix=prefix,
        verbose=verbose,
        quiet=quiet,
    )
    return v_3d_xclust_sim_execute(params, execution)


__all__ = [
    "V3dXclustSimOutputs",
    "V3dXclustSimParameters",
    "V_3D_XCLUST_SIM_METADATA",
    "v_3d_xclust_sim",
    "v_3d_xclust_sim_params",
]
