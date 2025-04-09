# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LONG_MRIS_SLOPES_METADATA = Metadata(
    id="903e6a1c3ac8764aca75012352e745ee5613437e.boutiques",
    name="long_mris_slopes",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


LongMrisSlopesParameters = typing.TypedDict('LongMrisSlopesParameters', {
    "__STYX_TYPE__": typing.Literal["long_mris_slopes"],
    "qdec": InputPathType,
    "meas": str,
    "hemi": str,
    "sd": str,
    "do_avg": bool,
    "do_rate": bool,
    "do_pc1fit": bool,
    "do_pc1": bool,
    "do_spc": bool,
    "do_stack": bool,
    "do_label": bool,
    "qcache": typing.NotRequired[str | None],
    "resid": typing.NotRequired[str | None],
    "fwhm": typing.NotRequired[str | None],
    "nosmooth": bool,
    "time": typing.NotRequired[str | None],
    "generic_time": bool,
    "in_label": typing.NotRequired[str | None],
    "jac": bool,
    "name_avg": typing.NotRequired[str | None],
    "name_rate": typing.NotRequired[str | None],
    "name_pc1fit": typing.NotRequired[str | None],
    "name_pc1": typing.NotRequired[str | None],
    "name_spc": typing.NotRequired[str | None],
    "name_resid": typing.NotRequired[str | None],
    "out_stack": typing.NotRequired[str | None],
    "out_label": typing.NotRequired[str | None],
    "isec_labels": typing.NotRequired[str | None],
    "stack_avg": typing.NotRequired[str | None],
    "stack_rate": typing.NotRequired[str | None],
    "stack_pc1fit": typing.NotRequired[str | None],
    "stack_pc1": typing.NotRequired[str | None],
    "stack_spc": typing.NotRequired[str | None],
    "stack_resid": typing.NotRequired[str | None],
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
        "long_mris_slopes": long_mris_slopes_cargs,
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


class LongMrisSlopesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `long_mris_slopes(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def long_mris_slopes_params(
    qdec: InputPathType,
    meas: str,
    hemi: str,
    sd: str,
    do_avg: bool = False,
    do_rate: bool = False,
    do_pc1fit: bool = False,
    do_pc1: bool = False,
    do_spc: bool = False,
    do_stack: bool = False,
    do_label: bool = False,
    qcache: str | None = None,
    resid: str | None = None,
    fwhm: str | None = None,
    nosmooth: bool = False,
    time_: str | None = None,
    generic_time: bool = False,
    in_label: str | None = None,
    jac: bool = False,
    name_avg: str | None = None,
    name_rate: str | None = None,
    name_pc1fit: str | None = None,
    name_pc1: str | None = None,
    name_spc: str | None = None,
    name_resid: str | None = None,
    out_stack: str | None = None,
    out_label: str | None = None,
    isec_labels: str | None = None,
    stack_avg: str | None = None,
    stack_rate: str | None = None,
    stack_pc1fit: str | None = None,
    stack_pc1: str | None = None,
    stack_spc: str | None = None,
    stack_resid: str | None = None,
) -> LongMrisSlopesParameters:
    """
    Build parameters.
    
    Args:
        qdec: (REQUIRED) QDEC table file specifying the subjects and time\
            points.
        meas: (REQUIRED) The surface input measure (e.g. thickness).
        hemi: (REQUIRED) Run one hemisphere: lh or rh or both.
        sd: (REQUIRED) Full path to FreeSurfer subjects directory.
        do_avg: Compute and output the temporal average.
        do_rate: Compute and output the rate.
        do_pc1fit: Compute and output the percent change (w.r.t. tp1 from\
            linear fit).
        do_pc1: Compute and output the percent change (w.r.t. tp1).
        do_spc: Compute and output the symmetrized percent change (w.r.t.\
            temporal average).
        do_stack: Save the stacked within subject file (time series).
        do_label: Compute and output intersected cortex label.
        qcache: Create cache for QDEC (resample to subject <QCACHE>, e.g.\
            fsaverage).
        resid: Residual time point (pass 1 for tp1 etc., pass 0 for average) to\
            export.
        fwhm: Smoothing at specific FWHM (required for percent change).
        nosmooth: Do not smooth the data.
        time_: Variable name for time column variable (e.g. age) in QDEC table.
        generic_time: Time points are ordered in QDEC file, assume\
            time=1,2,3...
        in_label: Use pre-existing label for smoothing and to mask the output.
        jac: Use this flag when mapping area or volume maps to correct Jacobian.
        name_avg: Filename (without hemi ?h) to store temporal average.
        name_rate: Filename (without hemi ?h) to store rate.
        name_pc1fit: Filename (without hemi ?h) to store percent change fit.
        name_pc1: Filename (without hemi ?h) to store percent change.
        name_spc: Filename (without hemi ?h) to store symmetrized percent\
            change.
        name_resid: Filename (without hemi ?h) to store residual.
        out_stack: Filename to store stacked measure file.
        out_label: Filename to store within-subject intersected cortex labels.
        isec_labels: Intersect labels on <qtarget> (usually cortex labels).
        stack_avg: Output stacked avg maps on <qtarget>.
        stack_rate: Output stacked rate maps on <qtarget>.
        stack_pc1fit: Output stacked PC1FIT maps on <qtarget>.
        stack_pc1: Output stacked PC1 maps on <qtarget>.
        stack_spc: Output stacked SPC maps on <qtarget>.
        stack_resid: Output stacked residual maps on <qtarget>.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "long_mris_slopes",
        "qdec": qdec,
        "meas": meas,
        "hemi": hemi,
        "sd": sd,
        "do_avg": do_avg,
        "do_rate": do_rate,
        "do_pc1fit": do_pc1fit,
        "do_pc1": do_pc1,
        "do_spc": do_spc,
        "do_stack": do_stack,
        "do_label": do_label,
        "nosmooth": nosmooth,
        "generic_time": generic_time,
        "jac": jac,
    }
    if qcache is not None:
        params["qcache"] = qcache
    if resid is not None:
        params["resid"] = resid
    if fwhm is not None:
        params["fwhm"] = fwhm
    if time_ is not None:
        params["time"] = time_
    if in_label is not None:
        params["in_label"] = in_label
    if name_avg is not None:
        params["name_avg"] = name_avg
    if name_rate is not None:
        params["name_rate"] = name_rate
    if name_pc1fit is not None:
        params["name_pc1fit"] = name_pc1fit
    if name_pc1 is not None:
        params["name_pc1"] = name_pc1
    if name_spc is not None:
        params["name_spc"] = name_spc
    if name_resid is not None:
        params["name_resid"] = name_resid
    if out_stack is not None:
        params["out_stack"] = out_stack
    if out_label is not None:
        params["out_label"] = out_label
    if isec_labels is not None:
        params["isec_labels"] = isec_labels
    if stack_avg is not None:
        params["stack_avg"] = stack_avg
    if stack_rate is not None:
        params["stack_rate"] = stack_rate
    if stack_pc1fit is not None:
        params["stack_pc1fit"] = stack_pc1fit
    if stack_pc1 is not None:
        params["stack_pc1"] = stack_pc1
    if stack_spc is not None:
        params["stack_spc"] = stack_spc
    if stack_resid is not None:
        params["stack_resid"] = stack_resid
    return params


def long_mris_slopes_cargs(
    params: LongMrisSlopesParameters,
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
    cargs.append("long_mris_slopes")
    cargs.extend([
        "--qdec",
        execution.input_file(params.get("qdec"))
    ])
    cargs.extend([
        "--meas",
        params.get("meas")
    ])
    cargs.extend([
        "--hemi",
        params.get("hemi")
    ])
    cargs.extend([
        "--sd",
        params.get("sd")
    ])
    if params.get("do_avg"):
        cargs.append("--do-avg")
    if params.get("do_rate"):
        cargs.append("--do-rate")
    if params.get("do_pc1fit"):
        cargs.append("--do-pc1fit")
    if params.get("do_pc1"):
        cargs.append("--do-pc1")
    if params.get("do_spc"):
        cargs.append("--do-spc")
    if params.get("do_stack"):
        cargs.append("--do-stack")
    if params.get("do_label"):
        cargs.append("--do-label")
    if params.get("qcache") is not None:
        cargs.extend([
            "--qcache",
            params.get("qcache")
        ])
    if params.get("resid") is not None:
        cargs.extend([
            "--resid",
            params.get("resid")
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "--fwhm",
            params.get("fwhm")
        ])
    if params.get("nosmooth"):
        cargs.append("--nosmooth")
    if params.get("time") is not None:
        cargs.extend([
            "--time",
            params.get("time")
        ])
    if params.get("generic_time"):
        cargs.append("--generic-time")
    if params.get("in_label") is not None:
        cargs.extend([
            "--in-label",
            params.get("in_label")
        ])
    if params.get("jac"):
        cargs.append("--jac")
    if params.get("name_avg") is not None:
        cargs.extend([
            "--name-avg",
            params.get("name_avg")
        ])
    if params.get("name_rate") is not None:
        cargs.extend([
            "--name-rate",
            params.get("name_rate")
        ])
    if params.get("name_pc1fit") is not None:
        cargs.extend([
            "--name-pc1fit",
            params.get("name_pc1fit")
        ])
    if params.get("name_pc1") is not None:
        cargs.extend([
            "--name-pc1",
            params.get("name_pc1")
        ])
    if params.get("name_spc") is not None:
        cargs.extend([
            "--name-spc",
            params.get("name_spc")
        ])
    if params.get("name_resid") is not None:
        cargs.extend([
            "--name-resid",
            params.get("name_resid")
        ])
    if params.get("out_stack") is not None:
        cargs.extend([
            "--out-stack",
            params.get("out_stack")
        ])
    if params.get("out_label") is not None:
        cargs.extend([
            "--out-label",
            params.get("out_label")
        ])
    if params.get("isec_labels") is not None:
        cargs.extend([
            "--isec-labels",
            params.get("isec_labels")
        ])
    if params.get("stack_avg") is not None:
        cargs.extend([
            "--stack-avg",
            params.get("stack_avg")
        ])
    if params.get("stack_rate") is not None:
        cargs.extend([
            "--stack-rate",
            params.get("stack_rate")
        ])
    if params.get("stack_pc1fit") is not None:
        cargs.extend([
            "--stack-pc1fit",
            params.get("stack_pc1fit")
        ])
    if params.get("stack_pc1") is not None:
        cargs.extend([
            "--stack-pc1",
            params.get("stack_pc1")
        ])
    if params.get("stack_spc") is not None:
        cargs.extend([
            "--stack-spc",
            params.get("stack_spc")
        ])
    if params.get("stack_resid") is not None:
        cargs.extend([
            "--stack-resid",
            params.get("stack_resid")
        ])
    return cargs


def long_mris_slopes_outputs(
    params: LongMrisSlopesParameters,
    execution: Execution,
) -> LongMrisSlopesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LongMrisSlopesOutputs(
        root=execution.output_file("."),
    )
    return ret


def long_mris_slopes_execute(
    params: LongMrisSlopesParameters,
    execution: Execution,
) -> LongMrisSlopesOutputs:
    """
    Computes slope maps (e.g., of thickness) in a longitudinal study using
    FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LongMrisSlopesOutputs`).
    """
    params = execution.params(params)
    cargs = long_mris_slopes_cargs(params, execution)
    ret = long_mris_slopes_outputs(params, execution)
    execution.run(cargs)
    return ret


def long_mris_slopes(
    qdec: InputPathType,
    meas: str,
    hemi: str,
    sd: str,
    do_avg: bool = False,
    do_rate: bool = False,
    do_pc1fit: bool = False,
    do_pc1: bool = False,
    do_spc: bool = False,
    do_stack: bool = False,
    do_label: bool = False,
    qcache: str | None = None,
    resid: str | None = None,
    fwhm: str | None = None,
    nosmooth: bool = False,
    time_: str | None = None,
    generic_time: bool = False,
    in_label: str | None = None,
    jac: bool = False,
    name_avg: str | None = None,
    name_rate: str | None = None,
    name_pc1fit: str | None = None,
    name_pc1: str | None = None,
    name_spc: str | None = None,
    name_resid: str | None = None,
    out_stack: str | None = None,
    out_label: str | None = None,
    isec_labels: str | None = None,
    stack_avg: str | None = None,
    stack_rate: str | None = None,
    stack_pc1fit: str | None = None,
    stack_pc1: str | None = None,
    stack_spc: str | None = None,
    stack_resid: str | None = None,
    runner: Runner | None = None,
) -> LongMrisSlopesOutputs:
    """
    Computes slope maps (e.g., of thickness) in a longitudinal study using
    FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        qdec: (REQUIRED) QDEC table file specifying the subjects and time\
            points.
        meas: (REQUIRED) The surface input measure (e.g. thickness).
        hemi: (REQUIRED) Run one hemisphere: lh or rh or both.
        sd: (REQUIRED) Full path to FreeSurfer subjects directory.
        do_avg: Compute and output the temporal average.
        do_rate: Compute and output the rate.
        do_pc1fit: Compute and output the percent change (w.r.t. tp1 from\
            linear fit).
        do_pc1: Compute and output the percent change (w.r.t. tp1).
        do_spc: Compute and output the symmetrized percent change (w.r.t.\
            temporal average).
        do_stack: Save the stacked within subject file (time series).
        do_label: Compute and output intersected cortex label.
        qcache: Create cache for QDEC (resample to subject <QCACHE>, e.g.\
            fsaverage).
        resid: Residual time point (pass 1 for tp1 etc., pass 0 for average) to\
            export.
        fwhm: Smoothing at specific FWHM (required for percent change).
        nosmooth: Do not smooth the data.
        time_: Variable name for time column variable (e.g. age) in QDEC table.
        generic_time: Time points are ordered in QDEC file, assume\
            time=1,2,3...
        in_label: Use pre-existing label for smoothing and to mask the output.
        jac: Use this flag when mapping area or volume maps to correct Jacobian.
        name_avg: Filename (without hemi ?h) to store temporal average.
        name_rate: Filename (without hemi ?h) to store rate.
        name_pc1fit: Filename (without hemi ?h) to store percent change fit.
        name_pc1: Filename (without hemi ?h) to store percent change.
        name_spc: Filename (without hemi ?h) to store symmetrized percent\
            change.
        name_resid: Filename (without hemi ?h) to store residual.
        out_stack: Filename to store stacked measure file.
        out_label: Filename to store within-subject intersected cortex labels.
        isec_labels: Intersect labels on <qtarget> (usually cortex labels).
        stack_avg: Output stacked avg maps on <qtarget>.
        stack_rate: Output stacked rate maps on <qtarget>.
        stack_pc1fit: Output stacked PC1FIT maps on <qtarget>.
        stack_pc1: Output stacked PC1 maps on <qtarget>.
        stack_spc: Output stacked SPC maps on <qtarget>.
        stack_resid: Output stacked residual maps on <qtarget>.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LongMrisSlopesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LONG_MRIS_SLOPES_METADATA)
    params = long_mris_slopes_params(
        qdec=qdec,
        meas=meas,
        hemi=hemi,
        sd=sd,
        do_avg=do_avg,
        do_rate=do_rate,
        do_pc1fit=do_pc1fit,
        do_pc1=do_pc1,
        do_spc=do_spc,
        do_stack=do_stack,
        do_label=do_label,
        qcache=qcache,
        resid=resid,
        fwhm=fwhm,
        nosmooth=nosmooth,
        time_=time_,
        generic_time=generic_time,
        in_label=in_label,
        jac=jac,
        name_avg=name_avg,
        name_rate=name_rate,
        name_pc1fit=name_pc1fit,
        name_pc1=name_pc1,
        name_spc=name_spc,
        name_resid=name_resid,
        out_stack=out_stack,
        out_label=out_label,
        isec_labels=isec_labels,
        stack_avg=stack_avg,
        stack_rate=stack_rate,
        stack_pc1fit=stack_pc1fit,
        stack_pc1=stack_pc1,
        stack_spc=stack_spc,
        stack_resid=stack_resid,
    )
    return long_mris_slopes_execute(params, execution)


__all__ = [
    "LONG_MRIS_SLOPES_METADATA",
    "LongMrisSlopesOutputs",
    "LongMrisSlopesParameters",
    "long_mris_slopes",
    "long_mris_slopes_params",
]
