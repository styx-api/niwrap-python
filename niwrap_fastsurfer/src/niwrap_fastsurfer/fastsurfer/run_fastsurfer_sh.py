# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RUN_FASTSURFER_SH_METADATA = Metadata(
    id="16844320fdd509dd7f0092a139a8a74ff8fc083a.boutiques",
    name="run_fastsurfer.sh",
    package="fastsurfer",
    container_image_tag="deepmi/fastsurfer:cpu-v2.3.3",
)


RunFastsurferShParameters = typing.TypedDict('RunFastsurferShParameters', {
    "__STYXTYPE__": typing.Literal["run_fastsurfer.sh"],
    "sid": str,
    "subjects_dir": str,
    "t1_input": InputPathType,
    "fs_license": typing.NotRequired[InputPathType | None],
    "asegdkt_segfile": typing.NotRequired[str | None],
    "vox_size": typing.NotRequired[str | None],
    "seg_only": bool,
    "seg_log": typing.NotRequired[str | None],
    "conformed_name": typing.NotRequired[str | None],
    "norm_name": typing.NotRequired[str | None],
    "t2_input": typing.NotRequired[InputPathType | None],
    "reg_mode": typing.NotRequired[typing.Literal["none", "coreg", "robust"] | None],
    "threads": typing.NotRequired[int | None],
    "device": typing.NotRequired[str | None],
    "viewagg_device": typing.NotRequired[str | None],
    "batch_size": typing.NotRequired[int | None],
    "python_cmd": typing.NotRequired[str | None],
    "surf_only": bool,
    "no_biasfield": bool,
    "tal_reg": bool,
    "no_asegdkt": bool,
    "no_cereb": bool,
    "cereb_segfile": typing.NotRequired[str | None],
    "no_hypothal": bool,
    "qc_snap": bool,
    "three_t": bool,
    "parallel": bool,
    "ignore_fs_version": bool,
    "fstess": bool,
    "fsqsphere": bool,
    "fsaparc": bool,
    "no_fs_t1": bool,
    "no_surfreg": bool,
    "allow_root": bool,
    "version": typing.NotRequired[str | None],
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
        "run_fastsurfer.sh": run_fastsurfer_sh_cargs,
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
        "run_fastsurfer.sh": run_fastsurfer_sh_outputs,
    }.get(t)


class RunFastsurferShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_fastsurfer_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation: OutputPathType
    """FastSurferVINN segmentation output"""
    surface_files: OutputPathType
    """Generated surface files"""
    cerebellum_seg: OutputPathType
    """Cerebellum segmentation output"""
    qc_snapshots: OutputPathType
    """Quality control snapshot images"""
    bias_corrected: OutputPathType
    """Bias field corrected image"""


def run_fastsurfer_sh_params(
    sid: str,
    subjects_dir: str,
    t1_input: InputPathType,
    fs_license: InputPathType | None = None,
    asegdkt_segfile: str | None = None,
    vox_size: str | None = None,
    seg_only: bool = False,
    seg_log: str | None = None,
    conformed_name: str | None = None,
    norm_name: str | None = None,
    t2_input: InputPathType | None = None,
    reg_mode: typing.Literal["none", "coreg", "robust"] | None = None,
    threads: int | None = None,
    device: str | None = None,
    viewagg_device: str | None = None,
    batch_size: int | None = 1,
    python_cmd: str | None = "python3.10 -s",
    surf_only: bool = False,
    no_biasfield: bool = False,
    tal_reg: bool = False,
    no_asegdkt: bool = False,
    no_cereb: bool = False,
    cereb_segfile: str | None = None,
    no_hypothal: bool = False,
    qc_snap: bool = False,
    three_t: bool = False,
    parallel: bool = False,
    ignore_fs_version: bool = False,
    fstess: bool = False,
    fsqsphere: bool = False,
    fsaparc: bool = False,
    no_fs_t1: bool = False,
    no_surfreg: bool = False,
    allow_root: bool = False,
    version: str | None = None,
) -> RunFastsurferShParameters:
    """
    Build parameters.
    
    Args:
        sid: Subject ID to create directory inside SUBJECTS_DIR.
        subjects_dir: Output directory SUBJECTS_DIR.
        t1_input: T1 full head input (not bias corrected). Requires an ABSOLUTE\
            Path!.
        fs_license: Path to FreeSurfer license key file.
        asegdkt_segfile: Name of the segmentation file including\
            aparc+DKTatlas-aseg segmentations.
        vox_size: Forces processing at a specific voxel size (0.7-1 or 'min').
        seg_only: Run only FastSurferVINN.
        seg_log: Log-file for the segmentation.
        conformed_name: Name of the file for the conformed input image.
        norm_name: Name of the biasfield corrected image.
        t2_input: Optional T2 full head input.
        reg_mode: Registration method for T1 and T2 images.
        threads: Set openMP and ITK threads.
        device: Device for inference (cpu/cuda).
        viewagg_device: Device for view aggregation.
        batch_size: Batch size for inference.
        python_cmd: Command for python.
        surf_only: Run surface pipeline only.
        no_biasfield: Deactivate bias field correction and partial\
            volume-corrected stats.
        tal_reg: Perform talairach registration for eTIV estimates.
        no_asegdkt: Skip the asegdkt segmentation.
        no_cereb: Skip the cerebellum segmentation.
        cereb_segfile: Name of DL-based segmentation file of the cerebellum.
        no_hypothal: Skip the hypothalamus segmentation.
        qc_snap: Create QC snapshots in subjects directory.
        three_t: Use the 3T atlas for talairach registration.
        parallel: Run both hemispheres in parallel.
        ignore_fs_version: Switch on to avoid check for FreeSurfer version.
        fstess: Switch on mri_tesselate for surface creation.
        fsqsphere: Use FreeSurfer iterative inflation for qsphere.
        fsaparc: Additionally create FS aparc segmentations and ribbon.
        no_fs_t1: Do not generate T1.mgz.
        no_surfreg: Do not run Surface registration with FreeSurfer.
        allow_root: Allow execution as root user.
        version: Print version information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "run_fastsurfer.sh",
        "sid": sid,
        "subjects_dir": subjects_dir,
        "t1_input": t1_input,
        "seg_only": seg_only,
        "surf_only": surf_only,
        "no_biasfield": no_biasfield,
        "tal_reg": tal_reg,
        "no_asegdkt": no_asegdkt,
        "no_cereb": no_cereb,
        "no_hypothal": no_hypothal,
        "qc_snap": qc_snap,
        "three_t": three_t,
        "parallel": parallel,
        "ignore_fs_version": ignore_fs_version,
        "fstess": fstess,
        "fsqsphere": fsqsphere,
        "fsaparc": fsaparc,
        "no_fs_t1": no_fs_t1,
        "no_surfreg": no_surfreg,
        "allow_root": allow_root,
    }
    if fs_license is not None:
        params["fs_license"] = fs_license
    if asegdkt_segfile is not None:
        params["asegdkt_segfile"] = asegdkt_segfile
    if vox_size is not None:
        params["vox_size"] = vox_size
    if seg_log is not None:
        params["seg_log"] = seg_log
    if conformed_name is not None:
        params["conformed_name"] = conformed_name
    if norm_name is not None:
        params["norm_name"] = norm_name
    if t2_input is not None:
        params["t2_input"] = t2_input
    if reg_mode is not None:
        params["reg_mode"] = reg_mode
    if threads is not None:
        params["threads"] = threads
    if device is not None:
        params["device"] = device
    if viewagg_device is not None:
        params["viewagg_device"] = viewagg_device
    if batch_size is not None:
        params["batch_size"] = batch_size
    if python_cmd is not None:
        params["python_cmd"] = python_cmd
    if cereb_segfile is not None:
        params["cereb_segfile"] = cereb_segfile
    if version is not None:
        params["version"] = version
    return params


def run_fastsurfer_sh_cargs(
    params: RunFastsurferShParameters,
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
    cargs.append("run_fastsurfer.sh")
    cargs.extend([
        "--sid",
        params.get("sid")
    ])
    cargs.extend([
        "--sd",
        params.get("subjects_dir")
    ])
    cargs.extend([
        "--t1",
        execution.input_file(params.get("t1_input"))
    ])
    if params.get("fs_license") is not None:
        cargs.extend([
            "--fs_license",
            execution.input_file(params.get("fs_license"))
        ])
    if params.get("asegdkt_segfile") is not None:
        cargs.extend([
            "--asegdkt_segfile",
            params.get("asegdkt_segfile")
        ])
    if params.get("vox_size") is not None:
        cargs.extend([
            "--vox_size",
            params.get("vox_size")
        ])
    if params.get("seg_only"):
        cargs.append("--seg_only")
    if params.get("seg_log") is not None:
        cargs.extend([
            "--seg_log",
            params.get("seg_log")
        ])
    if params.get("conformed_name") is not None:
        cargs.extend([
            "--conformed_name",
            params.get("conformed_name")
        ])
    if params.get("norm_name") is not None:
        cargs.extend([
            "--norm_name",
            params.get("norm_name")
        ])
    if params.get("t2_input") is not None:
        cargs.extend([
            "--t2",
            execution.input_file(params.get("t2_input"))
        ])
    if params.get("reg_mode") is not None:
        cargs.extend([
            "--reg_mode",
            params.get("reg_mode")
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("device") is not None:
        cargs.extend([
            "--device",
            params.get("device")
        ])
    if params.get("viewagg_device") is not None:
        cargs.extend([
            "--viewagg_device",
            params.get("viewagg_device")
        ])
    if params.get("batch_size") is not None:
        cargs.extend([
            "--batch",
            str(params.get("batch_size"))
        ])
    if params.get("python_cmd") is not None:
        cargs.extend([
            "--py",
            params.get("python_cmd")
        ])
    if params.get("surf_only"):
        cargs.append("--surf_only")
    if params.get("no_biasfield"):
        cargs.append("--no_biasfield")
    if params.get("tal_reg"):
        cargs.append("--tal_reg")
    if params.get("no_asegdkt"):
        cargs.append("--no_asegdkt")
    if params.get("no_cereb"):
        cargs.append("--no_cereb")
    if params.get("cereb_segfile") is not None:
        cargs.extend([
            "--cereb_segfile",
            params.get("cereb_segfile")
        ])
    if params.get("no_hypothal"):
        cargs.append("--no_hypothal")
    if params.get("qc_snap"):
        cargs.append("--qc_snap")
    if params.get("three_t"):
        cargs.append("--3T")
    if params.get("parallel"):
        cargs.append("--parallel")
    if params.get("ignore_fs_version"):
        cargs.append("--ignore_fs_version")
    if params.get("fstess"):
        cargs.append("--fstess")
    if params.get("fsqsphere"):
        cargs.append("--fsqsphere")
    if params.get("fsaparc"):
        cargs.append("--fsaparc")
    if params.get("no_fs_t1"):
        cargs.append("--no_fs_T1")
    if params.get("no_surfreg"):
        cargs.append("--no_surfreg")
    if params.get("allow_root"):
        cargs.append("--allow_root")
    if params.get("version") is not None:
        cargs.extend([
            "--version",
            params.get("version")
        ])
    return cargs


def run_fastsurfer_sh_outputs(
    params: RunFastsurferShParameters,
    execution: Execution,
) -> RunFastsurferShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RunFastsurferShOutputs(
        root=execution.output_file("."),
        segmentation=execution.output_file(params.get("subjects_dir") + "/" + params.get("sid") + "/mri/aparc.DKTatlas+aseg.deep.mgz"),
        surface_files=execution.output_file(params.get("subjects_dir") + "/" + params.get("sid") + "/surf/"),
        cerebellum_seg=execution.output_file(params.get("subjects_dir") + "/" + params.get("sid") + "/mri/cerebellum.CerebNet.nii.gz"),
        qc_snapshots=execution.output_file(params.get("subjects_dir") + "/" + params.get("sid") + "/qc_snapshots/"),
        bias_corrected=execution.output_file(params.get("subjects_dir") + "/" + params.get("sid") + "/mri/orig_nu.mgz"),
    )
    return ret


def run_fastsurfer_sh_execute(
    params: RunFastsurferShParameters,
    execution: Execution,
) -> RunFastsurferShOutputs:
    """
    run_fastsurfer.sh takes a T1 full head image and creates segmentation using
    FastSurferVINN and surfaces using recon-surf.
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RunFastsurferShOutputs`).
    """
    params = execution.params(params)
    cargs = run_fastsurfer_sh_cargs(params, execution)
    ret = run_fastsurfer_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def run_fastsurfer_sh(
    sid: str,
    subjects_dir: str,
    t1_input: InputPathType,
    fs_license: InputPathType | None = None,
    asegdkt_segfile: str | None = None,
    vox_size: str | None = None,
    seg_only: bool = False,
    seg_log: str | None = None,
    conformed_name: str | None = None,
    norm_name: str | None = None,
    t2_input: InputPathType | None = None,
    reg_mode: typing.Literal["none", "coreg", "robust"] | None = None,
    threads: int | None = None,
    device: str | None = None,
    viewagg_device: str | None = None,
    batch_size: int | None = 1,
    python_cmd: str | None = "python3.10 -s",
    surf_only: bool = False,
    no_biasfield: bool = False,
    tal_reg: bool = False,
    no_asegdkt: bool = False,
    no_cereb: bool = False,
    cereb_segfile: str | None = None,
    no_hypothal: bool = False,
    qc_snap: bool = False,
    three_t: bool = False,
    parallel: bool = False,
    ignore_fs_version: bool = False,
    fstess: bool = False,
    fsqsphere: bool = False,
    fsaparc: bool = False,
    no_fs_t1: bool = False,
    no_surfreg: bool = False,
    allow_root: bool = False,
    version: str | None = None,
    runner: Runner | None = None,
) -> RunFastsurferShOutputs:
    """
    run_fastsurfer.sh takes a T1 full head image and creates segmentation using
    FastSurferVINN and surfaces using recon-surf.
    
    Args:
        sid: Subject ID to create directory inside SUBJECTS_DIR.
        subjects_dir: Output directory SUBJECTS_DIR.
        t1_input: T1 full head input (not bias corrected). Requires an ABSOLUTE\
            Path!.
        fs_license: Path to FreeSurfer license key file.
        asegdkt_segfile: Name of the segmentation file including\
            aparc+DKTatlas-aseg segmentations.
        vox_size: Forces processing at a specific voxel size (0.7-1 or 'min').
        seg_only: Run only FastSurferVINN.
        seg_log: Log-file for the segmentation.
        conformed_name: Name of the file for the conformed input image.
        norm_name: Name of the biasfield corrected image.
        t2_input: Optional T2 full head input.
        reg_mode: Registration method for T1 and T2 images.
        threads: Set openMP and ITK threads.
        device: Device for inference (cpu/cuda).
        viewagg_device: Device for view aggregation.
        batch_size: Batch size for inference.
        python_cmd: Command for python.
        surf_only: Run surface pipeline only.
        no_biasfield: Deactivate bias field correction and partial\
            volume-corrected stats.
        tal_reg: Perform talairach registration for eTIV estimates.
        no_asegdkt: Skip the asegdkt segmentation.
        no_cereb: Skip the cerebellum segmentation.
        cereb_segfile: Name of DL-based segmentation file of the cerebellum.
        no_hypothal: Skip the hypothalamus segmentation.
        qc_snap: Create QC snapshots in subjects directory.
        three_t: Use the 3T atlas for talairach registration.
        parallel: Run both hemispheres in parallel.
        ignore_fs_version: Switch on to avoid check for FreeSurfer version.
        fstess: Switch on mri_tesselate for surface creation.
        fsqsphere: Use FreeSurfer iterative inflation for qsphere.
        fsaparc: Additionally create FS aparc segmentations and ribbon.
        no_fs_t1: Do not generate T1.mgz.
        no_surfreg: Do not run Surface registration with FreeSurfer.
        allow_root: Allow execution as root user.
        version: Print version information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunFastsurferShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_FASTSURFER_SH_METADATA)
    params = run_fastsurfer_sh_params(
        sid=sid,
        subjects_dir=subjects_dir,
        t1_input=t1_input,
        fs_license=fs_license,
        asegdkt_segfile=asegdkt_segfile,
        vox_size=vox_size,
        seg_only=seg_only,
        seg_log=seg_log,
        conformed_name=conformed_name,
        norm_name=norm_name,
        t2_input=t2_input,
        reg_mode=reg_mode,
        threads=threads,
        device=device,
        viewagg_device=viewagg_device,
        batch_size=batch_size,
        python_cmd=python_cmd,
        surf_only=surf_only,
        no_biasfield=no_biasfield,
        tal_reg=tal_reg,
        no_asegdkt=no_asegdkt,
        no_cereb=no_cereb,
        cereb_segfile=cereb_segfile,
        no_hypothal=no_hypothal,
        qc_snap=qc_snap,
        three_t=three_t,
        parallel=parallel,
        ignore_fs_version=ignore_fs_version,
        fstess=fstess,
        fsqsphere=fsqsphere,
        fsaparc=fsaparc,
        no_fs_t1=no_fs_t1,
        no_surfreg=no_surfreg,
        allow_root=allow_root,
        version=version,
    )
    return run_fastsurfer_sh_execute(params, execution)


__all__ = [
    "RUN_FASTSURFER_SH_METADATA",
    "RunFastsurferShOutputs",
    "RunFastsurferShParameters",
    "run_fastsurfer_sh",
    "run_fastsurfer_sh_params",
]
