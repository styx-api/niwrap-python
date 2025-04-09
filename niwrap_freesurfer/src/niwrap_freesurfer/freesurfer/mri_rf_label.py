# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_RF_LABEL_METADATA = Metadata(
    id="f6a8f74bc20598512ca39566372ca9777024a7f0.boutiques",
    name="mri_rf_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriRfLabelParameters = typing.TypedDict('MriRfLabelParameters', {
    "__STYX_TYPE__": typing.Literal["mri_rf_label"],
    "input_volumes": list[InputPathType],
    "transform_file": InputPathType,
    "gcafile": InputPathType,
    "output_volume": str,
    "cross_sequence_flag": bool,
    "nogibbs_flag": bool,
    "wm_path": typing.NotRequired[InputPathType | None],
    "conform_flag": bool,
    "normpd_flag": bool,
    "gca_tl": typing.NotRequired[InputPathType | None],
    "debug_voxel": typing.NotRequired[list[float] | None],
    "debug_node": typing.NotRequired[list[float] | None],
    "debug_label": typing.NotRequired[float | None],
    "tr": typing.NotRequired[float | None],
    "te": typing.NotRequired[float | None],
    "alpha": typing.NotRequired[float | None],
    "example": typing.NotRequired[list[InputPathType] | None],
    "pthresh": typing.NotRequired[float | None],
    "niter": typing.NotRequired[float | None],
    "novar_flag": bool,
    "regularize": typing.NotRequired[float | None],
    "nohippo_flag": bool,
    "fwm": typing.NotRequired[InputPathType | None],
    "mri_vol": typing.NotRequired[InputPathType | None],
    "heq": typing.NotRequired[InputPathType | None],
    "renorm": typing.NotRequired[InputPathType | None],
    "flash_flag": bool,
    "flash_params": typing.NotRequired[InputPathType | None],
    "renormalize": typing.NotRequired[list[float] | None],
    "set_input": typing.NotRequired[InputPathType | None],
    "histogram_flag": bool,
    "cond_density_mean": typing.NotRequired[float | None],
    "snapshots": typing.NotRequired[list[str] | None],
    "mask": typing.NotRequired[InputPathType | None],
    "expand": typing.NotRequired[float | None],
    "max_iter": typing.NotRequired[float | None],
    "filter_mode": typing.NotRequired[list[float] | None],
    "longitudinal_vol": typing.NotRequired[InputPathType | None],
    "longitudinal_lta": typing.NotRequired[InputPathType | None],
    "relabel_unlikely_flag": typing.NotRequired[list[float] | None],
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
        "mri_rf_label": mri_rf_label_cargs,
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
        "mri_rf_label": mri_rf_label_outputs,
    }.get(t)


class MriRfLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_rf_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outvol: OutputPathType
    """Output volume from mri_ca_label"""


def mri_rf_label_params(
    input_volumes: list[InputPathType],
    transform_file: InputPathType,
    gcafile: InputPathType,
    output_volume: str,
    cross_sequence_flag: bool = False,
    nogibbs_flag: bool = False,
    wm_path: InputPathType | None = None,
    conform_flag: bool = False,
    normpd_flag: bool = False,
    gca_tl: InputPathType | None = None,
    debug_voxel: list[float] | None = None,
    debug_node: list[float] | None = None,
    debug_label: float | None = None,
    tr: float | None = None,
    te: float | None = None,
    alpha: float | None = None,
    example: list[InputPathType] | None = None,
    pthresh: float | None = 0.7,
    niter: float | None = 2,
    novar_flag: bool = False,
    regularize: float | None = None,
    nohippo_flag: bool = False,
    fwm: InputPathType | None = None,
    mri_vol: InputPathType | None = None,
    heq: InputPathType | None = None,
    renorm: InputPathType | None = None,
    flash_flag: bool = False,
    flash_params: InputPathType | None = None,
    renormalize: list[float] | None = None,
    set_input: InputPathType | None = None,
    histogram_flag: bool = False,
    cond_density_mean: float | None = None,
    snapshots: list[str] | None = None,
    mask: InputPathType | None = None,
    expand: float | None = None,
    max_iter: float | None = 200,
    filter_mode: list[float] | None = [0, 0.5],
    longitudinal_vol: InputPathType | None = None,
    longitudinal_lta: InputPathType | None = None,
    relabel_unlikely_flag: list[float] | None = None,
) -> MriRfLabelParameters:
    """
    Build parameters.
    
    Args:
        input_volumes: Input volume(s).
        transform_file: Transform file.
        gcafile: GCA file.
        output_volume: Output volume.
        cross_sequence_flag: Label a volume acquired with a sequence different\
            than atlas.
        nogibbs_flag: Disable gibbs priors.
        wm_path: Use WM segmentation from provided file.
        conform_flag: Interpolate volume to be isotropic 1mm^3.
        normpd_flag: Normalize PD image to GCA means.
        gca_tl: Use file to label the thin temporal lobe.
        debug_voxel: Debug voxel at specified coordinates.
        debug_node: Debug node at specified coordinates.
        debug_label: Debug label at specified index.
        tr: Set TR in msec.
        te: Set TE in msec.
        alpha: Set alpha in radians.
        example: Use T1 (mri_vol) and segmentation as example.
        pthresh: Use p threshold for adaptive renormalization.
        niter: Apply max likelihood for n iterations.
        novar_flag: Do not use variance in classification.
        regularize: Regularize variance to be sigma+nC(noise).
        nohippo_flag: Do not auto-edit hippocampus.
        fwm: Use fixed white matter segmentation from wm.
        mri_vol: Write most likely MR volume to specified file.
        heq: Use histogram equalization from specified volume.
        renorm: Renormalize using predicted intensity values.
        flash_flag: Use FLASH forward model to predict intensity values.
        flash_params: Use FLASH forward model and tissue params from file.
        renormalize: Renorm class means iter times after initial label with\
            window of wsize.
        set_input: Set input volume.
        histogram_flag: Use GCA to histogram normalize input image.
        cond_density_mean: Mean filter n times to conditional densities.
        snapshots: Write snapshots of gibbs process every n times to filename.
        mask: Use mri_vol to mask final labeling.
        expand: Expand.
        max_iter: Set max iterations.
        filter_mode: Filter labeled volume with threshold t mode filter f times.
        longitudinal_vol: Longitudinal processing: mri_vol is label from tp1,\
            LTA is registration from tp1 to current data.
        longitudinal_lta: Longitudinal LTA registration.
        relabel_unlikely_flag: Reclassify voxels using a Gaussian window to\
            recomute priors and likelihoods.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_rf_label",
        "input_volumes": input_volumes,
        "transform_file": transform_file,
        "gcafile": gcafile,
        "output_volume": output_volume,
        "cross_sequence_flag": cross_sequence_flag,
        "nogibbs_flag": nogibbs_flag,
        "conform_flag": conform_flag,
        "normpd_flag": normpd_flag,
        "novar_flag": novar_flag,
        "nohippo_flag": nohippo_flag,
        "flash_flag": flash_flag,
        "histogram_flag": histogram_flag,
    }
    if wm_path is not None:
        params["wm_path"] = wm_path
    if gca_tl is not None:
        params["gca_tl"] = gca_tl
    if debug_voxel is not None:
        params["debug_voxel"] = debug_voxel
    if debug_node is not None:
        params["debug_node"] = debug_node
    if debug_label is not None:
        params["debug_label"] = debug_label
    if tr is not None:
        params["tr"] = tr
    if te is not None:
        params["te"] = te
    if alpha is not None:
        params["alpha"] = alpha
    if example is not None:
        params["example"] = example
    if pthresh is not None:
        params["pthresh"] = pthresh
    if niter is not None:
        params["niter"] = niter
    if regularize is not None:
        params["regularize"] = regularize
    if fwm is not None:
        params["fwm"] = fwm
    if mri_vol is not None:
        params["mri_vol"] = mri_vol
    if heq is not None:
        params["heq"] = heq
    if renorm is not None:
        params["renorm"] = renorm
    if flash_params is not None:
        params["flash_params"] = flash_params
    if renormalize is not None:
        params["renormalize"] = renormalize
    if set_input is not None:
        params["set_input"] = set_input
    if cond_density_mean is not None:
        params["cond_density_mean"] = cond_density_mean
    if snapshots is not None:
        params["snapshots"] = snapshots
    if mask is not None:
        params["mask"] = mask
    if expand is not None:
        params["expand"] = expand
    if max_iter is not None:
        params["max_iter"] = max_iter
    if filter_mode is not None:
        params["filter_mode"] = filter_mode
    if longitudinal_vol is not None:
        params["longitudinal_vol"] = longitudinal_vol
    if longitudinal_lta is not None:
        params["longitudinal_lta"] = longitudinal_lta
    if relabel_unlikely_flag is not None:
        params["relabel_unlikely_flag"] = relabel_unlikely_flag
    return params


def mri_rf_label_cargs(
    params: MriRfLabelParameters,
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
    cargs.append("mri_rf_label")
    cargs.extend([execution.input_file(f) for f in params.get("input_volumes")])
    cargs.append(execution.input_file(params.get("transform_file")))
    cargs.append(execution.input_file(params.get("gcafile")))
    cargs.append(params.get("output_volume"))
    if params.get("cross_sequence_flag"):
        cargs.append("-cross-sequence")
    if params.get("nogibbs_flag"):
        cargs.append("-nogibbs")
    if params.get("wm_path") is not None:
        cargs.extend([
            "-wm",
            execution.input_file(params.get("wm_path"))
        ])
    if params.get("conform_flag"):
        cargs.append("-conform")
    if params.get("normpd_flag"):
        cargs.append("-normpd")
    if params.get("gca_tl") is not None:
        cargs.extend([
            "-tl",
            execution.input_file(params.get("gca_tl"))
        ])
    if params.get("debug_voxel") is not None:
        cargs.extend([
            "-debug_voxel",
            *map(str, params.get("debug_voxel"))
        ])
    if params.get("debug_node") is not None:
        cargs.extend([
            "-debug_node",
            *map(str, params.get("debug_node"))
        ])
    if params.get("debug_label") is not None:
        cargs.extend([
            "-debug_label",
            str(params.get("debug_label"))
        ])
    if params.get("tr") is not None:
        cargs.extend([
            "-tr",
            str(params.get("tr"))
        ])
    if params.get("te") is not None:
        cargs.extend([
            "-te",
            str(params.get("te"))
        ])
    if params.get("alpha") is not None:
        cargs.extend([
            "-alpha",
            str(params.get("alpha"))
        ])
    if params.get("example") is not None:
        cargs.extend([
            "-example",
            *[execution.input_file(f) for f in params.get("example")]
        ])
    if params.get("pthresh") is not None:
        cargs.extend([
            "-pthresh",
            str(params.get("pthresh"))
        ])
    if params.get("niter") is not None:
        cargs.extend([
            "-niter",
            str(params.get("niter"))
        ])
    if params.get("novar_flag"):
        cargs.append("-novar")
    if params.get("regularize") is not None:
        cargs.extend([
            "-regularize",
            str(params.get("regularize"))
        ])
    if params.get("nohippo_flag"):
        cargs.append("-nohippo")
    if params.get("fwm") is not None:
        cargs.extend([
            "-fwm",
            execution.input_file(params.get("fwm"))
        ])
    if params.get("mri_vol") is not None:
        cargs.extend([
            "-mri",
            execution.input_file(params.get("mri_vol"))
        ])
    if params.get("heq") is not None:
        cargs.extend([
            "-heq",
            execution.input_file(params.get("heq"))
        ])
    if params.get("renorm") is not None:
        cargs.extend([
            "-renorm",
            execution.input_file(params.get("renorm"))
        ])
    if params.get("flash_flag"):
        cargs.append("-flash")
    if params.get("flash_params") is not None:
        cargs.extend([
            "-flash_params",
            execution.input_file(params.get("flash_params"))
        ])
    if params.get("renormalize") is not None:
        cargs.extend([
            "-renormalize",
            *map(str, params.get("renormalize"))
        ])
    if params.get("set_input") is not None:
        cargs.extend([
            "-r",
            execution.input_file(params.get("set_input"))
        ])
    if params.get("histogram_flag"):
        cargs.append("-h")
    if params.get("cond_density_mean") is not None:
        cargs.extend([
            "-a",
            str(params.get("cond_density_mean"))
        ])
    if params.get("snapshots") is not None:
        cargs.extend([
            "-w",
            *params.get("snapshots")
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask"))
        ])
    if params.get("expand") is not None:
        cargs.extend([
            "-e",
            str(params.get("expand"))
        ])
    if params.get("max_iter") is not None:
        cargs.extend([
            "-n",
            str(params.get("max_iter"))
        ])
    if params.get("filter_mode") is not None:
        cargs.extend([
            "-f",
            *map(str, params.get("filter_mode"))
        ])
    if params.get("longitudinal_vol") is not None:
        cargs.extend([
            "-L",
            execution.input_file(params.get("longitudinal_vol"))
        ])
    if params.get("longitudinal_lta") is not None:
        cargs.append(execution.input_file(params.get("longitudinal_lta")))
    if params.get("relabel_unlikely_flag") is not None:
        cargs.extend([
            "-RELABEL_UNLIKELY",
            *map(str, params.get("relabel_unlikely_flag"))
        ])
    return cargs


def mri_rf_label_outputs(
    params: MriRfLabelParameters,
    execution: Execution,
) -> MriRfLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriRfLabelOutputs(
        root=execution.output_file("."),
        outvol=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_rf_label_execute(
    params: MriRfLabelParameters,
    execution: Execution,
) -> MriRfLabelOutputs:
    """
    MRI automatic tissue labeling using a Gaussian Classifier Atlas (GCA).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriRfLabelOutputs`).
    """
    params = execution.params(params)
    cargs = mri_rf_label_cargs(params, execution)
    ret = mri_rf_label_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_rf_label(
    input_volumes: list[InputPathType],
    transform_file: InputPathType,
    gcafile: InputPathType,
    output_volume: str,
    cross_sequence_flag: bool = False,
    nogibbs_flag: bool = False,
    wm_path: InputPathType | None = None,
    conform_flag: bool = False,
    normpd_flag: bool = False,
    gca_tl: InputPathType | None = None,
    debug_voxel: list[float] | None = None,
    debug_node: list[float] | None = None,
    debug_label: float | None = None,
    tr: float | None = None,
    te: float | None = None,
    alpha: float | None = None,
    example: list[InputPathType] | None = None,
    pthresh: float | None = 0.7,
    niter: float | None = 2,
    novar_flag: bool = False,
    regularize: float | None = None,
    nohippo_flag: bool = False,
    fwm: InputPathType | None = None,
    mri_vol: InputPathType | None = None,
    heq: InputPathType | None = None,
    renorm: InputPathType | None = None,
    flash_flag: bool = False,
    flash_params: InputPathType | None = None,
    renormalize: list[float] | None = None,
    set_input: InputPathType | None = None,
    histogram_flag: bool = False,
    cond_density_mean: float | None = None,
    snapshots: list[str] | None = None,
    mask: InputPathType | None = None,
    expand: float | None = None,
    max_iter: float | None = 200,
    filter_mode: list[float] | None = [0, 0.5],
    longitudinal_vol: InputPathType | None = None,
    longitudinal_lta: InputPathType | None = None,
    relabel_unlikely_flag: list[float] | None = None,
    runner: Runner | None = None,
) -> MriRfLabelOutputs:
    """
    MRI automatic tissue labeling using a Gaussian Classifier Atlas (GCA).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volumes: Input volume(s).
        transform_file: Transform file.
        gcafile: GCA file.
        output_volume: Output volume.
        cross_sequence_flag: Label a volume acquired with a sequence different\
            than atlas.
        nogibbs_flag: Disable gibbs priors.
        wm_path: Use WM segmentation from provided file.
        conform_flag: Interpolate volume to be isotropic 1mm^3.
        normpd_flag: Normalize PD image to GCA means.
        gca_tl: Use file to label the thin temporal lobe.
        debug_voxel: Debug voxel at specified coordinates.
        debug_node: Debug node at specified coordinates.
        debug_label: Debug label at specified index.
        tr: Set TR in msec.
        te: Set TE in msec.
        alpha: Set alpha in radians.
        example: Use T1 (mri_vol) and segmentation as example.
        pthresh: Use p threshold for adaptive renormalization.
        niter: Apply max likelihood for n iterations.
        novar_flag: Do not use variance in classification.
        regularize: Regularize variance to be sigma+nC(noise).
        nohippo_flag: Do not auto-edit hippocampus.
        fwm: Use fixed white matter segmentation from wm.
        mri_vol: Write most likely MR volume to specified file.
        heq: Use histogram equalization from specified volume.
        renorm: Renormalize using predicted intensity values.
        flash_flag: Use FLASH forward model to predict intensity values.
        flash_params: Use FLASH forward model and tissue params from file.
        renormalize: Renorm class means iter times after initial label with\
            window of wsize.
        set_input: Set input volume.
        histogram_flag: Use GCA to histogram normalize input image.
        cond_density_mean: Mean filter n times to conditional densities.
        snapshots: Write snapshots of gibbs process every n times to filename.
        mask: Use mri_vol to mask final labeling.
        expand: Expand.
        max_iter: Set max iterations.
        filter_mode: Filter labeled volume with threshold t mode filter f times.
        longitudinal_vol: Longitudinal processing: mri_vol is label from tp1,\
            LTA is registration from tp1 to current data.
        longitudinal_lta: Longitudinal LTA registration.
        relabel_unlikely_flag: Reclassify voxels using a Gaussian window to\
            recomute priors and likelihoods.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRfLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_RF_LABEL_METADATA)
    params = mri_rf_label_params(
        input_volumes=input_volumes,
        transform_file=transform_file,
        gcafile=gcafile,
        output_volume=output_volume,
        cross_sequence_flag=cross_sequence_flag,
        nogibbs_flag=nogibbs_flag,
        wm_path=wm_path,
        conform_flag=conform_flag,
        normpd_flag=normpd_flag,
        gca_tl=gca_tl,
        debug_voxel=debug_voxel,
        debug_node=debug_node,
        debug_label=debug_label,
        tr=tr,
        te=te,
        alpha=alpha,
        example=example,
        pthresh=pthresh,
        niter=niter,
        novar_flag=novar_flag,
        regularize=regularize,
        nohippo_flag=nohippo_flag,
        fwm=fwm,
        mri_vol=mri_vol,
        heq=heq,
        renorm=renorm,
        flash_flag=flash_flag,
        flash_params=flash_params,
        renormalize=renormalize,
        set_input=set_input,
        histogram_flag=histogram_flag,
        cond_density_mean=cond_density_mean,
        snapshots=snapshots,
        mask=mask,
        expand=expand,
        max_iter=max_iter,
        filter_mode=filter_mode,
        longitudinal_vol=longitudinal_vol,
        longitudinal_lta=longitudinal_lta,
        relabel_unlikely_flag=relabel_unlikely_flag,
    )
    return mri_rf_label_execute(params, execution)


__all__ = [
    "MRI_RF_LABEL_METADATA",
    "MriRfLabelOutputs",
    "MriRfLabelParameters",
    "mri_rf_label",
    "mri_rf_label_params",
]
