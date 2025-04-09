# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_GTMPVC_METADATA = Metadata(
    id="748c620f515c8c257f35efdcec5890b6f140a8fd.boutiques",
    name="mri_gtmpvc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriGtmpvcParameters = typing.TypedDict('MriGtmpvcParameters', {
    "__STYX_TYPE__": typing.Literal["mri_gtmpvc"],
    "input_volume": InputPathType,
    "frame": typing.NotRequired[float | None],
    "psf": float,
    "segmentation": InputPathType,
    "registration": typing.NotRequired[InputPathType | None],
    "regheader": bool,
    "reg_identity": bool,
    "output_directory": str,
    "mask": typing.NotRequired[InputPathType | None],
    "auto_mask": typing.NotRequired[int | None],
    "no_reduce_fov": bool,
    "reduce_fov_eqodd": bool,
    "contrast_matrix": typing.NotRequired[InputPathType | None],
    "default_seg_merge": bool,
    "merge_hypos": bool,
    "merge_cblum_wm_gyri": bool,
    "tt_reduce": bool,
    "replace_seg": typing.NotRequired[str | None],
    "replace_file": typing.NotRequired[InputPathType | None],
    "rescale": typing.NotRequired[str | None],
    "no_rescale": bool,
    "scale_refval": typing.NotRequired[float | None],
    "ctab": typing.NotRequired[InputPathType | None],
    "ctab_default": bool,
    "tt_update": bool,
    "lateralization": bool,
    "no_tfe": bool,
    "no_pvc": bool,
    "segpvfres": typing.NotRequired[float | None],
    "rbv": bool,
    "rbv_res": typing.NotRequired[float | None],
    "mueller_pvc": typing.NotRequired[str | None],
    "mg_ref_cerebral_wm": bool,
    "mg_ref_lobes_wm": bool,
    "glm_mg_pvc": typing.NotRequired[float | None],
    "km_ref": typing.NotRequired[str | None],
    "km_hb": typing.NotRequired[str | None],
    "steady_state": typing.NotRequired[str | None],
    "save_x": bool,
    "save_y": bool,
    "save_beta": bool,
    "save_x0": bool,
    "save_input": bool,
    "save_eres": bool,
    "save_yhat": bool,
    "save_yhat_noise": typing.NotRequired[str | None],
    "save_yhat_full_fov": bool,
    "save_yhat0": bool,
    "synth": typing.NotRequired[str | None],
    "synth_only": bool,
    "synth_save": bool,
    "save_text": bool,
    "threads": typing.NotRequired[float | None],
    "max_threads": bool,
    "max_threads_minus_one": bool,
    "subjects_dir": typing.NotRequired[str | None],
    "vg_thresh": typing.NotRequired[float | None],
    "gdiag": typing.NotRequired[float | None],
    "debug": bool,
    "checkopts": bool,
    "help": bool,
    "version": bool,
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
        "mri_gtmpvc": mri_gtmpvc_cargs,
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
        "mri_gtmpvc": mri_gtmpvc_outputs,
    }.get(t)


class MriGtmpvcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_gtmpvc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    synthesized_volume: OutputPathType
    """Synthesized volume"""
    rescaled_input: OutputPathType
    """Rescaled input volume"""
    eresiduals: OutputPathType
    """Residual errors volume"""
    yhat: OutputPathType
    """Yhat volume"""
    yhat_with_noise: OutputPathType
    """Yhat with noise volume"""
    yhat_full_fov: OutputPathType
    """Yhat full FoV volume"""
    yhat_prior: OutputPathType
    """Yhat prior to smoothing volume"""
    x_matrix: OutputPathType
    """X matrix in matlab4 format"""
    y_matrix: OutputPathType
    """Y matrix in matlab4 format"""
    beta_matrix: OutputPathType
    """Beta matrix in matlab4 format"""
    x0_matrix: OutputPathType
    """X0 matrix in matlab4 format"""
    gtm_values_text: OutputPathType
    """Demeaned GTM values as text file"""


def mri_gtmpvc_params(
    input_volume: InputPathType,
    psf: float,
    segmentation: InputPathType,
    output_directory: str,
    frame: float | None = None,
    registration: InputPathType | None = None,
    regheader: bool = False,
    reg_identity: bool = False,
    mask: InputPathType | None = None,
    auto_mask: int | None = None,
    no_reduce_fov: bool = False,
    reduce_fov_eqodd: bool = False,
    contrast_matrix: InputPathType | None = None,
    default_seg_merge: bool = False,
    merge_hypos: bool = False,
    merge_cblum_wm_gyri: bool = False,
    tt_reduce: bool = False,
    replace_seg: str | None = None,
    replace_file: InputPathType | None = None,
    rescale: str | None = None,
    no_rescale: bool = False,
    scale_refval: float | None = None,
    ctab: InputPathType | None = None,
    ctab_default: bool = False,
    tt_update: bool = False,
    lateralization: bool = False,
    no_tfe: bool = False,
    no_pvc: bool = False,
    segpvfres: float | None = None,
    rbv: bool = False,
    rbv_res: float | None = None,
    mueller_pvc: str | None = None,
    mg_ref_cerebral_wm: bool = False,
    mg_ref_lobes_wm: bool = False,
    glm_mg_pvc: float | None = None,
    km_ref: str | None = None,
    km_hb: str | None = None,
    steady_state: str | None = None,
    save_x: bool = False,
    save_y: bool = False,
    save_beta: bool = False,
    save_x0: bool = False,
    save_input: bool = False,
    save_eres: bool = False,
    save_yhat: bool = False,
    save_yhat_noise: str | None = None,
    save_yhat_full_fov: bool = False,
    save_yhat0: bool = False,
    synth: str | None = None,
    synth_only: bool = False,
    synth_save: bool = False,
    save_text: bool = False,
    threads: float | None = None,
    max_threads: bool = False,
    max_threads_minus_one: bool = False,
    subjects_dir: str | None = None,
    vg_thresh: float | None = None,
    gdiag: float | None = None,
    debug: bool = False,
    checkopts: bool = False,
    help_: bool = False,
    version: bool = False,
) -> MriGtmpvcParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input volume: source data to PVC.
        psf: Scanner PSF FWHM in mm.
        segmentation: Anatomical segmentation to define regions for GTM.
        output_directory: Output directory.
        frame: Only process 0-based frame F from input volume.
        registration: LTA registration file that maps PET to anatomical.
        regheader: Assume input and seg share scanner space.
        reg_identity: Assume that input is in anatomical space.
        mask: Ignore areas outside of the mask (in input vol space).
        auto_mask: Automatically compute mask with FWHM and threshold.
        no_reduce_fov: Do not reduce FoV to encompass mask.
        reduce_fov_eqodd: Reduce FoV to encompass mask but force nc=nr and ns\
            to be odd.
        contrast_matrix: Univariate contrast to test.
        default_seg_merge: Default schema for merging ROIs.
        merge_hypos: Merge left and right hypointensites into ROI.
        merge_cblum_wm_gyri: Cerebellum WM gyri back into cerebellum WM.
        tt_reduce: Reduce segmentation to that of a tissue type.
        replace_seg: Replace seg Id1 with seg Id2.
        replace_file: File with a list of Ids to replace.
        rescale: Specify reference region(s) used to rescale (default is pons).
        no_rescale: Do not global rescale such that mean of reference region is\
            scaleref.
        scale_refval: Scale such that mean in reference region is refval.
        ctab: Specify color table explicitly.
        ctab_default: Use default color table.
        tt_update: Changes tissue type of VentralDC, BrainStem, and Pons to be\
            SubcortGM.
        lateralization: Lateralize tissue types.
        no_tfe: Do not correct for tissue fraction effect.
        no_pvc: Turns off PVC entirely.
        segpvfres: Set the tissue fraction resolution parameter (default is\
            0.5).
        rbv: Perform RBV PVC.
        rbv_res: Set RBV voxel resolution.
        mueller_pvc: Perform Mueller-Gaertner PVC.
        mg_ref_cerebral_wm: Set MG RefIds to 2 and 41.
        mg_ref_lobes_wm: Set MG RefIds to those for lobes when using wm subseg.
        glm_mg_pvc: GLM-based Mueller-Gaertner PVC.
        km_ref: Compute reference TAC for KM as mean of given RefIds.
        km_hb: Compute HiBinding TAC for KM as mean of given RefIds.
        steady_state: Steady-state analysis spec blood plasma concentration,\
            unit scale, and decay correction factor.
        save_x: Save X matrix in matlab4 format as X.mat.
        save_y: Save y matrix in matlab4 format as y.mat.
        save_beta: Save beta matrix in matlab4 format as beta.mat.
        save_x0: Save X0 matrix in matlab4 format as X0.mat.
        save_input: Saves rescaled input as input.rescaled.nii.gz.
        save_eres: Saves residual error.
        save_yhat: Saves yhat.
        save_yhat_noise: Saves yhat with noise, seed < 0 for TOD.
        save_yhat_full_fov: Saves yhat in full FoV (if FoV was reduced).
        save_yhat0: Saves yhat prior to smoothing.
        synth: Synthesize volume with gtmbeta as input.
        synth_only: Exit after doing synthesis (implies --synth-save).
        synth_save: With --synth saves synthesized volume to\
            outdir/synth.nii.gz.
        save_text: Save demeaned GTM values out to text files named after the\
            seg.
        threads: Use N threads (with Open MP).
        max_threads: Use the maximum allowable number of threads for this\
            computer.
        max_threads_minus_one: Use one less than the maximum allowable number\
            of threads for this computer.
        subjects_dir: Specify SUBJECTS_DIR.
        vg_thresh: Threshold for LTAconcat error.
        gdiag: Set diagnostic level.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_gtmpvc",
        "input_volume": input_volume,
        "psf": psf,
        "segmentation": segmentation,
        "regheader": regheader,
        "reg_identity": reg_identity,
        "output_directory": output_directory,
        "no_reduce_fov": no_reduce_fov,
        "reduce_fov_eqodd": reduce_fov_eqodd,
        "default_seg_merge": default_seg_merge,
        "merge_hypos": merge_hypos,
        "merge_cblum_wm_gyri": merge_cblum_wm_gyri,
        "tt_reduce": tt_reduce,
        "no_rescale": no_rescale,
        "ctab_default": ctab_default,
        "tt_update": tt_update,
        "lateralization": lateralization,
        "no_tfe": no_tfe,
        "no_pvc": no_pvc,
        "rbv": rbv,
        "mg_ref_cerebral_wm": mg_ref_cerebral_wm,
        "mg_ref_lobes_wm": mg_ref_lobes_wm,
        "save_x": save_x,
        "save_y": save_y,
        "save_beta": save_beta,
        "save_x0": save_x0,
        "save_input": save_input,
        "save_eres": save_eres,
        "save_yhat": save_yhat,
        "save_yhat_full_fov": save_yhat_full_fov,
        "save_yhat0": save_yhat0,
        "synth_only": synth_only,
        "synth_save": synth_save,
        "save_text": save_text,
        "max_threads": max_threads,
        "max_threads_minus_one": max_threads_minus_one,
        "debug": debug,
        "checkopts": checkopts,
        "help": help_,
        "version": version,
    }
    if frame is not None:
        params["frame"] = frame
    if registration is not None:
        params["registration"] = registration
    if mask is not None:
        params["mask"] = mask
    if auto_mask is not None:
        params["auto_mask"] = auto_mask
    if contrast_matrix is not None:
        params["contrast_matrix"] = contrast_matrix
    if replace_seg is not None:
        params["replace_seg"] = replace_seg
    if replace_file is not None:
        params["replace_file"] = replace_file
    if rescale is not None:
        params["rescale"] = rescale
    if scale_refval is not None:
        params["scale_refval"] = scale_refval
    if ctab is not None:
        params["ctab"] = ctab
    if segpvfres is not None:
        params["segpvfres"] = segpvfres
    if rbv_res is not None:
        params["rbv_res"] = rbv_res
    if mueller_pvc is not None:
        params["mueller_pvc"] = mueller_pvc
    if glm_mg_pvc is not None:
        params["glm_mg_pvc"] = glm_mg_pvc
    if km_ref is not None:
        params["km_ref"] = km_ref
    if km_hb is not None:
        params["km_hb"] = km_hb
    if steady_state is not None:
        params["steady_state"] = steady_state
    if save_yhat_noise is not None:
        params["save_yhat_noise"] = save_yhat_noise
    if synth is not None:
        params["synth"] = synth
    if threads is not None:
        params["threads"] = threads
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if vg_thresh is not None:
        params["vg_thresh"] = vg_thresh
    if gdiag is not None:
        params["gdiag"] = gdiag
    return params


def mri_gtmpvc_cargs(
    params: MriGtmpvcParameters,
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
    cargs.append("mri_gtmpvc")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_volume"))
    ])
    if params.get("frame") is not None:
        cargs.extend([
            "--frame",
            str(params.get("frame"))
        ])
    cargs.extend([
        "--psf",
        str(params.get("psf"))
    ])
    cargs.extend([
        "--seg",
        execution.input_file(params.get("segmentation"))
    ])
    if params.get("registration") is not None:
        cargs.extend([
            "--reg",
            execution.input_file(params.get("registration"))
        ])
    if params.get("regheader"):
        cargs.append("--regheader")
    if params.get("reg_identity"):
        cargs.append("--reg-identity")
    cargs.extend([
        "--o",
        params.get("output_directory")
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("auto_mask") is not None:
        cargs.extend([
            "--auto-mask",
            str(params.get("auto_mask"))
        ])
    if params.get("no_reduce_fov"):
        cargs.append("--no-reduce-fov")
    if params.get("reduce_fov_eqodd"):
        cargs.append("--reduce-fov-eqodd")
    if params.get("contrast_matrix") is not None:
        cargs.extend([
            "--C",
            execution.input_file(params.get("contrast_matrix"))
        ])
    if params.get("default_seg_merge"):
        cargs.append("--default-seg-merge")
    if params.get("merge_hypos"):
        cargs.append("--merge-hypos")
    if params.get("merge_cblum_wm_gyri"):
        cargs.append("--merge-cblum-wm-gyri")
    if params.get("tt_reduce"):
        cargs.append("--tt-reduce")
    if params.get("replace_seg") is not None:
        cargs.extend([
            "--replace",
            params.get("replace_seg")
        ])
    if params.get("replace_file") is not None:
        cargs.extend([
            "--replace-file",
            execution.input_file(params.get("replace_file"))
        ])
    if params.get("rescale") is not None:
        cargs.extend([
            "--rescale",
            params.get("rescale")
        ])
    if params.get("no_rescale"):
        cargs.append("--no-rescale")
    if params.get("scale_refval") is not None:
        cargs.extend([
            "--scale-refval",
            str(params.get("scale_refval"))
        ])
    if params.get("ctab") is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(params.get("ctab"))
        ])
    if params.get("ctab_default"):
        cargs.append("--ctab-default")
    if params.get("tt_update"):
        cargs.append("--tt-update")
    if params.get("lateralization"):
        cargs.append("--lat")
    if params.get("no_tfe"):
        cargs.append("--no-tfe")
    if params.get("no_pvc"):
        cargs.append("--no-pvc")
    if params.get("segpvfres") is not None:
        cargs.extend([
            "--segpvfres",
            str(params.get("segpvfres"))
        ])
    if params.get("rbv"):
        cargs.append("--rbv")
    if params.get("rbv_res") is not None:
        cargs.extend([
            "--rbv-res",
            str(params.get("rbv_res"))
        ])
    if params.get("mueller_pvc") is not None:
        cargs.extend([
            "--mg",
            params.get("mueller_pvc")
        ])
    if params.get("mg_ref_cerebral_wm"):
        cargs.append("--mg-ref-cerebral-wm")
    if params.get("mg_ref_lobes_wm"):
        cargs.append("--mg-ref-lobes-wm")
    if params.get("glm_mg_pvc") is not None:
        cargs.extend([
            "--mgx",
            str(params.get("glm_mg_pvc"))
        ])
    if params.get("km_ref") is not None:
        cargs.extend([
            "--km-ref",
            params.get("km_ref")
        ])
    if params.get("km_hb") is not None:
        cargs.extend([
            "--km-hb",
            params.get("km_hb")
        ])
    if params.get("steady_state") is not None:
        cargs.extend([
            "--ss",
            params.get("steady_state")
        ])
    if params.get("save_x"):
        cargs.append("--X")
    if params.get("save_y"):
        cargs.append("--y")
    if params.get("save_beta"):
        cargs.append("--beta")
    if params.get("save_x0"):
        cargs.append("--X0")
    if params.get("save_input"):
        cargs.append("--save-input")
    if params.get("save_eres"):
        cargs.append("--save-eres")
    if params.get("save_yhat"):
        cargs.append("--save-yhat")
    if params.get("save_yhat_noise") is not None:
        cargs.extend([
            "--save-yhat-with-noise",
            params.get("save_yhat_noise")
        ])
    if params.get("save_yhat_full_fov"):
        cargs.append("--save-yhat-full-fov")
    if params.get("save_yhat0"):
        cargs.append("--save-yhat0")
    if params.get("synth") is not None:
        cargs.extend([
            "--synth",
            params.get("synth")
        ])
    if params.get("synth_only"):
        cargs.append("--synth-only")
    if params.get("synth_save"):
        cargs.append("--synth-save")
    if params.get("save_text"):
        cargs.append("--save-text")
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("max_threads"):
        cargs.append("--max-threads")
    if params.get("max_threads_minus_one"):
        cargs.append("--max-threads-minus-1")
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("vg_thresh") is not None:
        cargs.extend([
            "--vg-thresh",
            str(params.get("vg_thresh"))
        ])
    if params.get("gdiag") is not None:
        cargs.extend([
            "--gdiag",
            str(params.get("gdiag"))
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def mri_gtmpvc_outputs(
    params: MriGtmpvcParameters,
    execution: Execution,
) -> MriGtmpvcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriGtmpvcOutputs(
        root=execution.output_file("."),
        synthesized_volume=execution.output_file(params.get("output_directory") + "/synth.nii.gz"),
        rescaled_input=execution.output_file(params.get("output_directory") + "/input.rescaled.nii.gz"),
        eresiduals=execution.output_file(params.get("output_directory") + "/eresiduals.nii.gz"),
        yhat=execution.output_file(params.get("output_directory") + "/yhat.nii.gz"),
        yhat_with_noise=execution.output_file(params.get("output_directory") + "/yhat_with_noise.nii.gz"),
        yhat_full_fov=execution.output_file(params.get("output_directory") + "/yhat_full_fov.nii.gz"),
        yhat_prior=execution.output_file(params.get("output_directory") + "/yhat_prior.nii.gz"),
        x_matrix=execution.output_file(params.get("output_directory") + "/X.mat"),
        y_matrix=execution.output_file(params.get("output_directory") + "/y.mat"),
        beta_matrix=execution.output_file(params.get("output_directory") + "/beta.mat"),
        x0_matrix=execution.output_file(params.get("output_directory") + "/X0.mat"),
        gtm_values_text=execution.output_file(params.get("output_directory") + "/gtm_values.txt"),
    )
    return ret


def mri_gtmpvc_execute(
    params: MriGtmpvcParameters,
    execution: Execution,
) -> MriGtmpvcOutputs:
    """
    mri_gtmpvc performs partial volume correction on PET data using anatomical
    segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriGtmpvcOutputs`).
    """
    params = execution.params(params)
    cargs = mri_gtmpvc_cargs(params, execution)
    ret = mri_gtmpvc_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_gtmpvc(
    input_volume: InputPathType,
    psf: float,
    segmentation: InputPathType,
    output_directory: str,
    frame: float | None = None,
    registration: InputPathType | None = None,
    regheader: bool = False,
    reg_identity: bool = False,
    mask: InputPathType | None = None,
    auto_mask: int | None = None,
    no_reduce_fov: bool = False,
    reduce_fov_eqodd: bool = False,
    contrast_matrix: InputPathType | None = None,
    default_seg_merge: bool = False,
    merge_hypos: bool = False,
    merge_cblum_wm_gyri: bool = False,
    tt_reduce: bool = False,
    replace_seg: str | None = None,
    replace_file: InputPathType | None = None,
    rescale: str | None = None,
    no_rescale: bool = False,
    scale_refval: float | None = None,
    ctab: InputPathType | None = None,
    ctab_default: bool = False,
    tt_update: bool = False,
    lateralization: bool = False,
    no_tfe: bool = False,
    no_pvc: bool = False,
    segpvfres: float | None = None,
    rbv: bool = False,
    rbv_res: float | None = None,
    mueller_pvc: str | None = None,
    mg_ref_cerebral_wm: bool = False,
    mg_ref_lobes_wm: bool = False,
    glm_mg_pvc: float | None = None,
    km_ref: str | None = None,
    km_hb: str | None = None,
    steady_state: str | None = None,
    save_x: bool = False,
    save_y: bool = False,
    save_beta: bool = False,
    save_x0: bool = False,
    save_input: bool = False,
    save_eres: bool = False,
    save_yhat: bool = False,
    save_yhat_noise: str | None = None,
    save_yhat_full_fov: bool = False,
    save_yhat0: bool = False,
    synth: str | None = None,
    synth_only: bool = False,
    synth_save: bool = False,
    save_text: bool = False,
    threads: float | None = None,
    max_threads: bool = False,
    max_threads_minus_one: bool = False,
    subjects_dir: str | None = None,
    vg_thresh: float | None = None,
    gdiag: float | None = None,
    debug: bool = False,
    checkopts: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriGtmpvcOutputs:
    """
    mri_gtmpvc performs partial volume correction on PET data using anatomical
    segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume: source data to PVC.
        psf: Scanner PSF FWHM in mm.
        segmentation: Anatomical segmentation to define regions for GTM.
        output_directory: Output directory.
        frame: Only process 0-based frame F from input volume.
        registration: LTA registration file that maps PET to anatomical.
        regheader: Assume input and seg share scanner space.
        reg_identity: Assume that input is in anatomical space.
        mask: Ignore areas outside of the mask (in input vol space).
        auto_mask: Automatically compute mask with FWHM and threshold.
        no_reduce_fov: Do not reduce FoV to encompass mask.
        reduce_fov_eqodd: Reduce FoV to encompass mask but force nc=nr and ns\
            to be odd.
        contrast_matrix: Univariate contrast to test.
        default_seg_merge: Default schema for merging ROIs.
        merge_hypos: Merge left and right hypointensites into ROI.
        merge_cblum_wm_gyri: Cerebellum WM gyri back into cerebellum WM.
        tt_reduce: Reduce segmentation to that of a tissue type.
        replace_seg: Replace seg Id1 with seg Id2.
        replace_file: File with a list of Ids to replace.
        rescale: Specify reference region(s) used to rescale (default is pons).
        no_rescale: Do not global rescale such that mean of reference region is\
            scaleref.
        scale_refval: Scale such that mean in reference region is refval.
        ctab: Specify color table explicitly.
        ctab_default: Use default color table.
        tt_update: Changes tissue type of VentralDC, BrainStem, and Pons to be\
            SubcortGM.
        lateralization: Lateralize tissue types.
        no_tfe: Do not correct for tissue fraction effect.
        no_pvc: Turns off PVC entirely.
        segpvfres: Set the tissue fraction resolution parameter (default is\
            0.5).
        rbv: Perform RBV PVC.
        rbv_res: Set RBV voxel resolution.
        mueller_pvc: Perform Mueller-Gaertner PVC.
        mg_ref_cerebral_wm: Set MG RefIds to 2 and 41.
        mg_ref_lobes_wm: Set MG RefIds to those for lobes when using wm subseg.
        glm_mg_pvc: GLM-based Mueller-Gaertner PVC.
        km_ref: Compute reference TAC for KM as mean of given RefIds.
        km_hb: Compute HiBinding TAC for KM as mean of given RefIds.
        steady_state: Steady-state analysis spec blood plasma concentration,\
            unit scale, and decay correction factor.
        save_x: Save X matrix in matlab4 format as X.mat.
        save_y: Save y matrix in matlab4 format as y.mat.
        save_beta: Save beta matrix in matlab4 format as beta.mat.
        save_x0: Save X0 matrix in matlab4 format as X0.mat.
        save_input: Saves rescaled input as input.rescaled.nii.gz.
        save_eres: Saves residual error.
        save_yhat: Saves yhat.
        save_yhat_noise: Saves yhat with noise, seed < 0 for TOD.
        save_yhat_full_fov: Saves yhat in full FoV (if FoV was reduced).
        save_yhat0: Saves yhat prior to smoothing.
        synth: Synthesize volume with gtmbeta as input.
        synth_only: Exit after doing synthesis (implies --synth-save).
        synth_save: With --synth saves synthesized volume to\
            outdir/synth.nii.gz.
        save_text: Save demeaned GTM values out to text files named after the\
            seg.
        threads: Use N threads (with Open MP).
        max_threads: Use the maximum allowable number of threads for this\
            computer.
        max_threads_minus_one: Use one less than the maximum allowable number\
            of threads for this computer.
        subjects_dir: Specify SUBJECTS_DIR.
        vg_thresh: Threshold for LTAconcat error.
        gdiag: Set diagnostic level.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriGtmpvcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_GTMPVC_METADATA)
    params = mri_gtmpvc_params(
        input_volume=input_volume,
        frame=frame,
        psf=psf,
        segmentation=segmentation,
        registration=registration,
        regheader=regheader,
        reg_identity=reg_identity,
        output_directory=output_directory,
        mask=mask,
        auto_mask=auto_mask,
        no_reduce_fov=no_reduce_fov,
        reduce_fov_eqodd=reduce_fov_eqodd,
        contrast_matrix=contrast_matrix,
        default_seg_merge=default_seg_merge,
        merge_hypos=merge_hypos,
        merge_cblum_wm_gyri=merge_cblum_wm_gyri,
        tt_reduce=tt_reduce,
        replace_seg=replace_seg,
        replace_file=replace_file,
        rescale=rescale,
        no_rescale=no_rescale,
        scale_refval=scale_refval,
        ctab=ctab,
        ctab_default=ctab_default,
        tt_update=tt_update,
        lateralization=lateralization,
        no_tfe=no_tfe,
        no_pvc=no_pvc,
        segpvfres=segpvfres,
        rbv=rbv,
        rbv_res=rbv_res,
        mueller_pvc=mueller_pvc,
        mg_ref_cerebral_wm=mg_ref_cerebral_wm,
        mg_ref_lobes_wm=mg_ref_lobes_wm,
        glm_mg_pvc=glm_mg_pvc,
        km_ref=km_ref,
        km_hb=km_hb,
        steady_state=steady_state,
        save_x=save_x,
        save_y=save_y,
        save_beta=save_beta,
        save_x0=save_x0,
        save_input=save_input,
        save_eres=save_eres,
        save_yhat=save_yhat,
        save_yhat_noise=save_yhat_noise,
        save_yhat_full_fov=save_yhat_full_fov,
        save_yhat0=save_yhat0,
        synth=synth,
        synth_only=synth_only,
        synth_save=synth_save,
        save_text=save_text,
        threads=threads,
        max_threads=max_threads,
        max_threads_minus_one=max_threads_minus_one,
        subjects_dir=subjects_dir,
        vg_thresh=vg_thresh,
        gdiag=gdiag,
        debug=debug,
        checkopts=checkopts,
        help_=help_,
        version=version,
    )
    return mri_gtmpvc_execute(params, execution)


__all__ = [
    "MRI_GTMPVC_METADATA",
    "MriGtmpvcOutputs",
    "MriGtmpvcParameters",
    "mri_gtmpvc",
    "mri_gtmpvc_params",
]
