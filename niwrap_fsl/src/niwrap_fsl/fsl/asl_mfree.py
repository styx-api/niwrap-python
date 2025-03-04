# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ASL_MFREE_METADATA = Metadata(
    id="2c6ac3df84ba3307596d4d4ee92da51804362ee6.boutiques",
    name="asl_mfree",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


AslMfreeParameters = typing.TypedDict('AslMfreeParameters', {
    "__STYX_TYPE__": typing.Literal["asl_mfree"],
    "datafile": InputPathType,
    "mask": InputPathType,
    "out": str,
    "aif": InputPathType,
    "dt": float,
    "metric": typing.NotRequired[InputPathType | None],
    "mthresh": typing.NotRequired[float | None],
    "tcorrect": bool,
    "bata": typing.NotRequired[InputPathType | None],
    "batt": typing.NotRequired[InputPathType | None],
    "bat": bool,
    "bat_grad_thr": typing.NotRequired[float | None],
    "t1": typing.NotRequired[float | None],
    "fa": typing.NotRequired[float | None],
    "std": bool,
    "nwb": typing.NotRequired[float | None],
    "turbo_quasar": bool,
    "shift_factor": typing.NotRequired[float | None],
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
        "asl_mfree": asl_mfree_cargs,
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
        "asl_mfree": asl_mfree_outputs,
    }.get(t)


class AslMfreeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `asl_mfree(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_file: OutputPathType
    """Output results from ASL model-free analysis"""
    bat_img: OutputPathType
    """Estimated tissue BAT image file"""


def asl_mfree_params(
    datafile: InputPathType,
    mask: InputPathType,
    out: str,
    aif: InputPathType,
    dt: float,
    metric: InputPathType | None = None,
    mthresh: float | None = None,
    tcorrect: bool = False,
    bata: InputPathType | None = None,
    batt: InputPathType | None = None,
    bat: bool = False,
    bat_grad_thr: float | None = 0.2,
    t1: float | None = None,
    fa: float | None = None,
    std: bool = False,
    nwb: float | None = None,
    turbo_quasar: bool = False,
    shift_factor: float | None = 1,
) -> AslMfreeParameters:
    """
    Build parameters.
    
    Args:
        datafile: ASL data file.
        mask: Mask file.
        out: Output directory name.
        aif: Arterial input functions for deconvolution (4D volume, one aif for\
            each voxel within mask).
        dt: Temporal spacing in data (s).
        metric: Metric image file (optional).
        mthresh: Metric threshold (optional).
        tcorrect: Apply correction for timing difference between AIF and tissue\
            curve (optional).
        bata: Arterial BAT image (optional).
        batt: Tissue BAT image (optional).
        bat: Estimate tissue BAT from data and save this image (optional).
        bat_grad_thr: Edge detection gradient threshold (default: 0.2,\
            optional).
        t1: T1 (of blood) value (optional).
        fa: Flip angle (if using LL readout, optional).
        std: Calculate standard deviations on perfusion values using wild\
            bootstrapping (optional).
        nwb: Number of permutations for wild bootstrapping (optional).
        turbo_quasar: Specify this is a Turbo QUASAR Sequence (optional).
        shift_factor: Slice shifting factor in Turbo QUASAR (default value: 1,\
            optional).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "asl_mfree",
        "datafile": datafile,
        "mask": mask,
        "out": out,
        "aif": aif,
        "dt": dt,
        "tcorrect": tcorrect,
        "bat": bat,
        "std": std,
        "turbo_quasar": turbo_quasar,
    }
    if metric is not None:
        params["metric"] = metric
    if mthresh is not None:
        params["mthresh"] = mthresh
    if bata is not None:
        params["bata"] = bata
    if batt is not None:
        params["batt"] = batt
    if bat_grad_thr is not None:
        params["bat_grad_thr"] = bat_grad_thr
    if t1 is not None:
        params["t1"] = t1
    if fa is not None:
        params["fa"] = fa
    if nwb is not None:
        params["nwb"] = nwb
    if shift_factor is not None:
        params["shift_factor"] = shift_factor
    return params


def asl_mfree_cargs(
    params: AslMfreeParameters,
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
    cargs.append("asl_mfree")
    cargs.extend([
        "--data",
        execution.input_file(params.get("datafile"))
    ])
    cargs.extend([
        "--mask",
        execution.input_file(params.get("mask"))
    ])
    cargs.extend([
        "--out",
        params.get("out")
    ])
    cargs.extend([
        "--aif",
        execution.input_file(params.get("aif"))
    ])
    cargs.extend([
        "--dt",
        str(params.get("dt"))
    ])
    if params.get("metric") is not None:
        cargs.extend([
            "--metric",
            execution.input_file(params.get("metric"))
        ])
    if params.get("mthresh") is not None:
        cargs.extend([
            "--mthresh",
            str(params.get("mthresh"))
        ])
    if params.get("tcorrect"):
        cargs.append("--tcorrect")
    if params.get("bata") is not None:
        cargs.extend([
            "--bata",
            execution.input_file(params.get("bata"))
        ])
    if params.get("batt") is not None:
        cargs.extend([
            "--batt",
            execution.input_file(params.get("batt"))
        ])
    if params.get("bat"):
        cargs.append("--bat")
    if params.get("bat_grad_thr") is not None:
        cargs.extend([
            "--bat_grad_thr",
            str(params.get("bat_grad_thr"))
        ])
    if params.get("t1") is not None:
        cargs.extend([
            "--t1",
            str(params.get("t1"))
        ])
    if params.get("fa") is not None:
        cargs.extend([
            "--fa",
            str(params.get("fa"))
        ])
    if params.get("std"):
        cargs.append("--std")
    if params.get("nwb") is not None:
        cargs.extend([
            "--nwb",
            str(params.get("nwb"))
        ])
    if params.get("turbo_quasar"):
        cargs.append("--turbo_quasar")
    if params.get("shift_factor") is not None:
        cargs.extend([
            "--shift_factor",
            str(params.get("shift_factor"))
        ])
    cargs.append("--verbose")
    return cargs


def asl_mfree_outputs(
    params: AslMfreeParameters,
    execution: Execution,
) -> AslMfreeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AslMfreeOutputs(
        root=execution.output_file("."),
        result_file=execution.output_file(params.get("out") + "/results.nii.gz"),
        bat_img=execution.output_file(params.get("out") + "/bat.nii.gz"),
    )
    return ret


def asl_mfree_execute(
    params: AslMfreeParameters,
    execution: Execution,
) -> AslMfreeOutputs:
    """
    ASL model-free analysis tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AslMfreeOutputs`).
    """
    params = execution.params(params)
    cargs = asl_mfree_cargs(params, execution)
    ret = asl_mfree_outputs(params, execution)
    execution.run(cargs)
    return ret


def asl_mfree(
    datafile: InputPathType,
    mask: InputPathType,
    out: str,
    aif: InputPathType,
    dt: float,
    metric: InputPathType | None = None,
    mthresh: float | None = None,
    tcorrect: bool = False,
    bata: InputPathType | None = None,
    batt: InputPathType | None = None,
    bat: bool = False,
    bat_grad_thr: float | None = 0.2,
    t1: float | None = None,
    fa: float | None = None,
    std: bool = False,
    nwb: float | None = None,
    turbo_quasar: bool = False,
    shift_factor: float | None = 1,
    runner: Runner | None = None,
) -> AslMfreeOutputs:
    """
    ASL model-free analysis tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        datafile: ASL data file.
        mask: Mask file.
        out: Output directory name.
        aif: Arterial input functions for deconvolution (4D volume, one aif for\
            each voxel within mask).
        dt: Temporal spacing in data (s).
        metric: Metric image file (optional).
        mthresh: Metric threshold (optional).
        tcorrect: Apply correction for timing difference between AIF and tissue\
            curve (optional).
        bata: Arterial BAT image (optional).
        batt: Tissue BAT image (optional).
        bat: Estimate tissue BAT from data and save this image (optional).
        bat_grad_thr: Edge detection gradient threshold (default: 0.2,\
            optional).
        t1: T1 (of blood) value (optional).
        fa: Flip angle (if using LL readout, optional).
        std: Calculate standard deviations on perfusion values using wild\
            bootstrapping (optional).
        nwb: Number of permutations for wild bootstrapping (optional).
        turbo_quasar: Specify this is a Turbo QUASAR Sequence (optional).
        shift_factor: Slice shifting factor in Turbo QUASAR (default value: 1,\
            optional).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AslMfreeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ASL_MFREE_METADATA)
    params = asl_mfree_params(
        datafile=datafile,
        mask=mask,
        out=out,
        aif=aif,
        dt=dt,
        metric=metric,
        mthresh=mthresh,
        tcorrect=tcorrect,
        bata=bata,
        batt=batt,
        bat=bat,
        bat_grad_thr=bat_grad_thr,
        t1=t1,
        fa=fa,
        std=std,
        nwb=nwb,
        turbo_quasar=turbo_quasar,
        shift_factor=shift_factor,
    )
    return asl_mfree_execute(params, execution)


__all__ = [
    "ASL_MFREE_METADATA",
    "AslMfreeOutputs",
    "AslMfreeParameters",
    "asl_mfree",
    "asl_mfree_params",
]
