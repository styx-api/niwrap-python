# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

EDDY_CUDA9_1_METADATA = Metadata(
    id="9c43f113da7bb1833918750386640a1fcb8b52e1.boutiques",
    name="eddy_cuda9.1",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


EddyCuda91Parameters = typing.TypedDict('EddyCuda91Parameters', {
    "__STYX_TYPE__": typing.Literal["eddy_cuda9.1"],
    "imain": InputPathType,
    "mask": InputPathType,
    "index": InputPathType,
    "acqp": InputPathType,
    "bvecs": InputPathType,
    "bvals": InputPathType,
    "out": str,
    "mb": typing.NotRequired[float | None],
    "mb_offs": typing.NotRequired[float | None],
    "slspec": typing.NotRequired[InputPathType | None],
    "json": typing.NotRequired[InputPathType | None],
    "mporder": typing.NotRequired[float | None],
    "s2v_lambda": typing.NotRequired[float | None],
    "topup": typing.NotRequired[InputPathType | None],
    "field": typing.NotRequired[InputPathType | None],
    "field_mat": typing.NotRequired[InputPathType | None],
    "flm": typing.NotRequired[typing.Literal["movement", "linear", "quadratic", "cubic"] | None],
    "slm": typing.NotRequired[typing.Literal["none", "linear", "quadratic"] | None],
    "fwhm": typing.NotRequired[float | None],
    "niter": typing.NotRequired[float | None],
    "s2v_niter": typing.NotRequired[float | None],
    "cnr_maps": bool,
    "residuals": bool,
    "fep": bool,
    "interp": typing.NotRequired[typing.Literal["spline", "trilinear"] | None],
    "s2v_interp": typing.NotRequired[typing.Literal["spline", "trilinear"] | None],
    "resamp": typing.NotRequired[typing.Literal["jac", "lsr"] | None],
    "nvoxhp": typing.NotRequired[float | None],
    "initrand": typing.NotRequired[float | None],
    "ff": typing.NotRequired[float | None],
    "repol": bool,
    "ol_nstd": typing.NotRequired[float | None],
    "ol_nvox": typing.NotRequired[float | None],
    "ol_type": typing.NotRequired[typing.Literal["sw", "gw", "both"] | None],
    "ol_pos": bool,
    "ol_sqr": bool,
    "estimate_move_by_susceptibility": bool,
    "mbs_niter": typing.NotRequired[float | None],
    "mbs_lambda": typing.NotRequired[float | None],
    "mbs_ksp": typing.NotRequired[float | None],
    "dont_sep_offs_move": bool,
    "dont_peas": bool,
    "data_is_shelled": bool,
    "verbose": bool,
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
        "eddy_cuda9.1": eddy_cuda9_1_cargs,
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
        "eddy_cuda9.1": eddy_cuda9_1_outputs,
    }.get(t)


class EddyCuda91Outputs(typing.NamedTuple):
    """
    Output object returned when calling `eddy_cuda9_1(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """Output file containing the corrected images"""
    eddy_parameters: OutputPathType
    """Text file containing subject movement and EC-induced field parameters for
    each volume"""
    rotated_bvecs: OutputPathType
    """File containing the reoriented b-vectors for diffusion analysis"""
    rotated_bvecs_slr: OutputPathType
    """File with rotated b-vectors for least-squares reconstruction"""
    command_txt: OutputPathType
    """Text file documenting the command line used to run eddy"""
    input_parameters: OutputPathType
    """List of all parameters used by eddy"""
    movement_rms: OutputPathType
    """Summary of total movement for each volume"""
    restricted_movement_rms: OutputPathType
    """Estimates movement RMS while disregarding translation in the PE
    direction"""
    shell_alignment_parameters: OutputPathType
    """Text file with rigid body movement parameters between different shells"""
    shell_pe_translation_parameters: OutputPathType
    """Translation parameters along the PE direction between different shells"""
    outlier_report: OutputPathType
    """Report of detected outlier slices"""
    outlier_map: OutputPathType
    """Numeric matrix indicating outlier slices"""
    outlier_n_stdev_map: OutputPathType
    """Map of the number of standard deviations for outliers"""
    outlier_n_sqr_stdev_map: OutputPathType
    """Map of the number of squared standard deviations for outliers"""
    outlier_free_data: OutputPathType
    """Original data with outlier slices replaced, only if --repol was set"""
    movement_over_time: OutputPathType
    """Text file with movement parameters over time, only if --mporder > 0"""
    mbs_first_order_fields: OutputPathType
    """4D image file of partial derivative fields, only if
    --estimate_move_by_susceptibility is set"""
    cnr_maps: OutputPathType
    """4D image file with SNR and CNR maps, only if --cnr_maps is set"""
    residuals: OutputPathType
    """4D image file of residuals, only if --residuals is set"""


def eddy_cuda9_1_params(
    imain: InputPathType,
    mask: InputPathType,
    index: InputPathType,
    acqp: InputPathType,
    bvecs: InputPathType,
    bvals: InputPathType,
    out: str = "eddy_corrected",
    mb: float | None = None,
    mb_offs: float | None = None,
    slspec: InputPathType | None = None,
    json_: InputPathType | None = None,
    mporder: float | None = None,
    s2v_lambda: float | None = None,
    topup: InputPathType | None = None,
    field: InputPathType | None = None,
    field_mat: InputPathType | None = None,
    flm: typing.Literal["movement", "linear", "quadratic", "cubic"] | None = None,
    slm: typing.Literal["none", "linear", "quadratic"] | None = None,
    fwhm: float | None = None,
    niter: float | None = None,
    s2v_niter: float | None = None,
    cnr_maps: bool = False,
    residuals: bool = False,
    fep: bool = False,
    interp: typing.Literal["spline", "trilinear"] | None = None,
    s2v_interp: typing.Literal["spline", "trilinear"] | None = None,
    resamp: typing.Literal["jac", "lsr"] | None = None,
    nvoxhp: float | None = None,
    initrand: float | None = None,
    ff: float | None = None,
    repol: bool = False,
    ol_nstd: float | None = None,
    ol_nvox: float | None = None,
    ol_type: typing.Literal["sw", "gw", "both"] | None = None,
    ol_pos: bool = False,
    ol_sqr: bool = False,
    estimate_move_by_susceptibility: bool = False,
    mbs_niter: float | None = None,
    mbs_lambda: float | None = None,
    mbs_ksp: float | None = None,
    dont_sep_offs_move: bool = False,
    dont_peas: bool = False,
    data_is_shelled: bool = False,
    verbose: bool = False,
) -> EddyCuda91Parameters:
    """
    Build parameters.
    
    Args:
        imain: File containing all the images to estimate distortions for.
        mask: Mask to indicate brain.
        index: File containing indices for all volumes in --imain into --acqp\
            and --topup.
        acqp: File containing acquisition parameters.
        bvecs: File containing the b-vectors for all volumes in --imain.
        bvals: File containing the b-values for all volumes in --imain.
        out: Basename for output.
        mb: Multi-band factor.
        mb_offs: Multi-band offset (-1 if bottom slice removed, 1 if top slice\
            removed).
        slspec: Name of text file completely specifying slice/group acuistion.\
            N.B. --slspec and --json are mutually exclusive.
        json_: Name of .json text file with information about slice timing.\
            N.B. --json and --slspec are mutually exclusive.
        mporder: Order of slice-to-vol movement model (default 0, i.e.\
            vol-to-vol.
        s2v_lambda: Regularisation weight for slice-to-vol movement. (default\
            1, reasonable range 1--10).
        topup: Base name for output files from topup.
        field: Name of file with susceptibility field (in Hz).
        field_mat: Name of rigid body transform for susceptibility field.
        flm: First level EC model (movement/linear/quadratic/cubic, default\
            quadratic).
        slm: Second level EC model (none/linear/quadratic, default none).
        fwhm: FWHM for conditioning filter when estimating the parameters\
            (default 0).
        niter: Number of iterations (default 5).
        s2v_niter: Number of iterations for slice-to-vol (default 5).
        cnr_maps: Write shell-wise cnr-maps (default false).
        residuals: Write residuals (between GP and observations), (default\
            false).
        fep: Fill empty planes in x- or y-directions (default false).
        interp: Interpolation model for estimation step (spline/trilinear,\
            default spline).
        s2v_interp: Slice-to-vol interpolation model for estimation step\
            (spline/trilinear, default trilinear).
        resamp: Final resampling method (jac/lsr, default jac).
        nvoxhp: # of voxels used to estimate the hyperparameters (default 1000).
        initrand: Seeds rand for when selecting voxels (default 0=no seeding).
        ff: Fudge factor for hyperparameter error variance (default 10.0).
        repol: Detect and replace outlier slices (default false)).
        ol_nstd: Number of std off to qualify as outlier (default 4).
        ol_nvox: Min # of voxels in a slice for inclusion in outlier detection\
            (default 250).
        ol_type: Type of outliers, slicewise (sw), groupwise (gw) or both\
            (both). (default sw).
        ol_pos: Consider both positive and negative outliers if set (default\
            false).
        ol_sqr: Consider outliers among sums-of-squared differences if set\
            (default false).
        estimate_move_by_susceptibility: Estimate how susceptibility field\
            changes with subject movement (default false).
        mbs_niter: Number of iterations for MBS estimation (default 10).
        mbs_lambda: Weighting of regularisation for MBS estimation (default 10).
        mbs_ksp: Knot-spacing for MBS field estimation (default 10mm).
        dont_sep_offs_move: Do NOT attempt to separate field offset from\
            subject movement (default false).
        dont_peas: Do NOT perform a post-eddy alignment of shells (default\
            false).
        data_is_shelled: Assume, don't check, that data is shelled (default\
            false).
        verbose: switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "eddy_cuda9.1",
        "imain": imain,
        "mask": mask,
        "index": index,
        "acqp": acqp,
        "bvecs": bvecs,
        "bvals": bvals,
        "out": out,
        "cnr_maps": cnr_maps,
        "residuals": residuals,
        "fep": fep,
        "repol": repol,
        "ol_pos": ol_pos,
        "ol_sqr": ol_sqr,
        "estimate_move_by_susceptibility": estimate_move_by_susceptibility,
        "dont_sep_offs_move": dont_sep_offs_move,
        "dont_peas": dont_peas,
        "data_is_shelled": data_is_shelled,
        "verbose": verbose,
    }
    if mb is not None:
        params["mb"] = mb
    if mb_offs is not None:
        params["mb_offs"] = mb_offs
    if slspec is not None:
        params["slspec"] = slspec
    if json_ is not None:
        params["json"] = json_
    if mporder is not None:
        params["mporder"] = mporder
    if s2v_lambda is not None:
        params["s2v_lambda"] = s2v_lambda
    if topup is not None:
        params["topup"] = topup
    if field is not None:
        params["field"] = field
    if field_mat is not None:
        params["field_mat"] = field_mat
    if flm is not None:
        params["flm"] = flm
    if slm is not None:
        params["slm"] = slm
    if fwhm is not None:
        params["fwhm"] = fwhm
    if niter is not None:
        params["niter"] = niter
    if s2v_niter is not None:
        params["s2v_niter"] = s2v_niter
    if interp is not None:
        params["interp"] = interp
    if s2v_interp is not None:
        params["s2v_interp"] = s2v_interp
    if resamp is not None:
        params["resamp"] = resamp
    if nvoxhp is not None:
        params["nvoxhp"] = nvoxhp
    if initrand is not None:
        params["initrand"] = initrand
    if ff is not None:
        params["ff"] = ff
    if ol_nstd is not None:
        params["ol_nstd"] = ol_nstd
    if ol_nvox is not None:
        params["ol_nvox"] = ol_nvox
    if ol_type is not None:
        params["ol_type"] = ol_type
    if mbs_niter is not None:
        params["mbs_niter"] = mbs_niter
    if mbs_lambda is not None:
        params["mbs_lambda"] = mbs_lambda
    if mbs_ksp is not None:
        params["mbs_ksp"] = mbs_ksp
    return params


def eddy_cuda9_1_cargs(
    params: EddyCuda91Parameters,
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
    cargs.append("eddy_cuda9.1")
    cargs.append("--imain=" + execution.input_file(params.get("imain")))
    cargs.append("--mask=" + execution.input_file(params.get("mask")))
    cargs.append("--index=" + execution.input_file(params.get("index")))
    cargs.append("--acqp=" + execution.input_file(params.get("acqp")))
    cargs.append("--bvecs=" + execution.input_file(params.get("bvecs")))
    cargs.append("--bvals=" + execution.input_file(params.get("bvals")))
    cargs.append("--out=" + params.get("out"))
    if params.get("mb") is not None:
        cargs.append("--mb=" + str(params.get("mb")))
    if params.get("mb_offs") is not None:
        cargs.append("--mb_offs=" + str(params.get("mb_offs")))
    if params.get("slspec") is not None:
        cargs.append("--slspec=" + execution.input_file(params.get("slspec")))
    if params.get("json") is not None:
        cargs.append("--json=" + execution.input_file(params.get("json")))
    if params.get("mporder") is not None:
        cargs.append("--mporder=" + str(params.get("mporder")))
    if params.get("s2v_lambda") is not None:
        cargs.append("--s2v_lambda=" + str(params.get("s2v_lambda")))
    if params.get("topup") is not None:
        cargs.append("--topup=" + execution.input_file(params.get("topup"), resolve_parent=True))
    if params.get("field") is not None:
        cargs.append("--field=" + execution.input_file(params.get("field")))
    if params.get("field_mat") is not None:
        cargs.append("--field_mat=" + execution.input_file(params.get("field_mat")))
    if params.get("flm") is not None:
        cargs.append("--flm=" + params.get("flm"))
    if params.get("slm") is not None:
        cargs.append("--slm=" + params.get("slm"))
    if params.get("fwhm") is not None:
        cargs.append("--fwhm=" + str(params.get("fwhm")))
    if params.get("niter") is not None:
        cargs.append("--niter=" + str(params.get("niter")))
    if params.get("s2v_niter") is not None:
        cargs.append("--s2v_niter=" + str(params.get("s2v_niter")))
    if params.get("cnr_maps"):
        cargs.append("--cnr_maps")
    if params.get("residuals"):
        cargs.append("--residuals")
    if params.get("fep"):
        cargs.append("--fep")
    if params.get("interp") is not None:
        cargs.append("--interp=" + params.get("interp"))
    if params.get("s2v_interp") is not None:
        cargs.append("--s2v_interp=" + params.get("s2v_interp"))
    if params.get("resamp") is not None:
        cargs.append("--resamp=" + params.get("resamp"))
    if params.get("nvoxhp") is not None:
        cargs.append("--nvoxhp=" + str(params.get("nvoxhp")))
    if params.get("initrand") is not None:
        cargs.append("--initrand=" + str(params.get("initrand")))
    if params.get("ff") is not None:
        cargs.append("--ff=" + str(params.get("ff")))
    if params.get("repol"):
        cargs.append("--repol")
    if params.get("ol_nstd") is not None:
        cargs.append("--ol_nstd=" + str(params.get("ol_nstd")))
    if params.get("ol_nvox") is not None:
        cargs.append("--ol_nvox=" + str(params.get("ol_nvox")))
    if params.get("ol_type") is not None:
        cargs.append("--ol_type=" + params.get("ol_type"))
    if params.get("ol_pos"):
        cargs.append("--ol_pos")
    if params.get("ol_sqr"):
        cargs.append("--ol_sqr")
    if params.get("estimate_move_by_susceptibility"):
        cargs.append("--estimate_move_by_susceptibility")
    if params.get("mbs_niter") is not None:
        cargs.append("--mbs_niter=" + str(params.get("mbs_niter")))
    if params.get("mbs_lambda") is not None:
        cargs.append("--mbs_lambda=" + str(params.get("mbs_lambda")))
    if params.get("mbs_ksp") is not None:
        cargs.append("--mbs_ksp=" + str(params.get("mbs_ksp")))
    if params.get("dont_sep_offs_move"):
        cargs.append("--dont_sep_offs_move")
    if params.get("dont_peas"):
        cargs.append("--dont_peas")
    if params.get("data_is_shelled"):
        cargs.append("--data_is_shelled")
    if params.get("verbose"):
        cargs.append("--verbose")
    return cargs


def eddy_cuda9_1_outputs(
    params: EddyCuda91Parameters,
    execution: Execution,
) -> EddyCuda91Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = EddyCuda91Outputs(
        root=execution.output_file("."),
        out=execution.output_file(params.get("out") + ".nii.gz"),
        eddy_parameters=execution.output_file(params.get("out") + ".eddy_parameters"),
        rotated_bvecs=execution.output_file(params.get("out") + ".eddy_rotated_bvecs"),
        rotated_bvecs_slr=execution.output_file(params.get("out") + ".eddy_rotated_bvecs_for_SLR"),
        command_txt=execution.output_file(params.get("out") + ".eddy_command_txt"),
        input_parameters=execution.output_file(params.get("out") + ".eddy_values_of_all_input_parameters"),
        movement_rms=execution.output_file(params.get("out") + ".eddy_movement_rms"),
        restricted_movement_rms=execution.output_file(params.get("out") + ".eddy_restricted_movement_rms"),
        shell_alignment_parameters=execution.output_file(params.get("out") + ".eddy_post_eddy_shell_alignment_parameters"),
        shell_pe_translation_parameters=execution.output_file(params.get("out") + ".eddy_post_eddy_shell_PE_translation_parameters"),
        outlier_report=execution.output_file(params.get("out") + ".eddy_outlier_report"),
        outlier_map=execution.output_file(params.get("out") + ".eddy_outlier_map"),
        outlier_n_stdev_map=execution.output_file(params.get("out") + ".eddy_outlier_n_stdev_map"),
        outlier_n_sqr_stdev_map=execution.output_file(params.get("out") + ".eddy_outlier_n_sqr_stdev_map"),
        outlier_free_data=execution.output_file(params.get("out") + ".eddy_outlier_free_data.nii.gz"),
        movement_over_time=execution.output_file(params.get("out") + ".eddy_movement_over_time"),
        mbs_first_order_fields=execution.output_file(params.get("out") + ".eddy_mbs_first_order_fields.nii.gz"),
        cnr_maps=execution.output_file(params.get("out") + ".eddy_cnr_maps"),
        residuals=execution.output_file(params.get("out") + ".eddy_residuals"),
    )
    return ret


def eddy_cuda9_1_execute(
    params: EddyCuda91Parameters,
    execution: Execution,
) -> EddyCuda91Outputs:
    """
    A tool for correcting eddy currents and movements in diffusion data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `EddyCuda91Outputs`).
    """
    params = execution.params(params)
    cargs = eddy_cuda9_1_cargs(params, execution)
    ret = eddy_cuda9_1_outputs(params, execution)
    execution.run(cargs)
    return ret


def eddy_cuda9_1(
    imain: InputPathType,
    mask: InputPathType,
    index: InputPathType,
    acqp: InputPathType,
    bvecs: InputPathType,
    bvals: InputPathType,
    out: str = "eddy_corrected",
    mb: float | None = None,
    mb_offs: float | None = None,
    slspec: InputPathType | None = None,
    json_: InputPathType | None = None,
    mporder: float | None = None,
    s2v_lambda: float | None = None,
    topup: InputPathType | None = None,
    field: InputPathType | None = None,
    field_mat: InputPathType | None = None,
    flm: typing.Literal["movement", "linear", "quadratic", "cubic"] | None = None,
    slm: typing.Literal["none", "linear", "quadratic"] | None = None,
    fwhm: float | None = None,
    niter: float | None = None,
    s2v_niter: float | None = None,
    cnr_maps: bool = False,
    residuals: bool = False,
    fep: bool = False,
    interp: typing.Literal["spline", "trilinear"] | None = None,
    s2v_interp: typing.Literal["spline", "trilinear"] | None = None,
    resamp: typing.Literal["jac", "lsr"] | None = None,
    nvoxhp: float | None = None,
    initrand: float | None = None,
    ff: float | None = None,
    repol: bool = False,
    ol_nstd: float | None = None,
    ol_nvox: float | None = None,
    ol_type: typing.Literal["sw", "gw", "both"] | None = None,
    ol_pos: bool = False,
    ol_sqr: bool = False,
    estimate_move_by_susceptibility: bool = False,
    mbs_niter: float | None = None,
    mbs_lambda: float | None = None,
    mbs_ksp: float | None = None,
    dont_sep_offs_move: bool = False,
    dont_peas: bool = False,
    data_is_shelled: bool = False,
    verbose: bool = False,
    runner: Runner | None = None,
) -> EddyCuda91Outputs:
    """
    A tool for correcting eddy currents and movements in diffusion data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        imain: File containing all the images to estimate distortions for.
        mask: Mask to indicate brain.
        index: File containing indices for all volumes in --imain into --acqp\
            and --topup.
        acqp: File containing acquisition parameters.
        bvecs: File containing the b-vectors for all volumes in --imain.
        bvals: File containing the b-values for all volumes in --imain.
        out: Basename for output.
        mb: Multi-band factor.
        mb_offs: Multi-band offset (-1 if bottom slice removed, 1 if top slice\
            removed).
        slspec: Name of text file completely specifying slice/group acuistion.\
            N.B. --slspec and --json are mutually exclusive.
        json_: Name of .json text file with information about slice timing.\
            N.B. --json and --slspec are mutually exclusive.
        mporder: Order of slice-to-vol movement model (default 0, i.e.\
            vol-to-vol.
        s2v_lambda: Regularisation weight for slice-to-vol movement. (default\
            1, reasonable range 1--10).
        topup: Base name for output files from topup.
        field: Name of file with susceptibility field (in Hz).
        field_mat: Name of rigid body transform for susceptibility field.
        flm: First level EC model (movement/linear/quadratic/cubic, default\
            quadratic).
        slm: Second level EC model (none/linear/quadratic, default none).
        fwhm: FWHM for conditioning filter when estimating the parameters\
            (default 0).
        niter: Number of iterations (default 5).
        s2v_niter: Number of iterations for slice-to-vol (default 5).
        cnr_maps: Write shell-wise cnr-maps (default false).
        residuals: Write residuals (between GP and observations), (default\
            false).
        fep: Fill empty planes in x- or y-directions (default false).
        interp: Interpolation model for estimation step (spline/trilinear,\
            default spline).
        s2v_interp: Slice-to-vol interpolation model for estimation step\
            (spline/trilinear, default trilinear).
        resamp: Final resampling method (jac/lsr, default jac).
        nvoxhp: # of voxels used to estimate the hyperparameters (default 1000).
        initrand: Seeds rand for when selecting voxels (default 0=no seeding).
        ff: Fudge factor for hyperparameter error variance (default 10.0).
        repol: Detect and replace outlier slices (default false)).
        ol_nstd: Number of std off to qualify as outlier (default 4).
        ol_nvox: Min # of voxels in a slice for inclusion in outlier detection\
            (default 250).
        ol_type: Type of outliers, slicewise (sw), groupwise (gw) or both\
            (both). (default sw).
        ol_pos: Consider both positive and negative outliers if set (default\
            false).
        ol_sqr: Consider outliers among sums-of-squared differences if set\
            (default false).
        estimate_move_by_susceptibility: Estimate how susceptibility field\
            changes with subject movement (default false).
        mbs_niter: Number of iterations for MBS estimation (default 10).
        mbs_lambda: Weighting of regularisation for MBS estimation (default 10).
        mbs_ksp: Knot-spacing for MBS field estimation (default 10mm).
        dont_sep_offs_move: Do NOT attempt to separate field offset from\
            subject movement (default false).
        dont_peas: Do NOT perform a post-eddy alignment of shells (default\
            false).
        data_is_shelled: Assume, don't check, that data is shelled (default\
            false).
        verbose: switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EddyCuda91Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EDDY_CUDA9_1_METADATA)
    params = eddy_cuda9_1_params(
        imain=imain,
        mask=mask,
        index=index,
        acqp=acqp,
        bvecs=bvecs,
        bvals=bvals,
        out=out,
        mb=mb,
        mb_offs=mb_offs,
        slspec=slspec,
        json_=json_,
        mporder=mporder,
        s2v_lambda=s2v_lambda,
        topup=topup,
        field=field,
        field_mat=field_mat,
        flm=flm,
        slm=slm,
        fwhm=fwhm,
        niter=niter,
        s2v_niter=s2v_niter,
        cnr_maps=cnr_maps,
        residuals=residuals,
        fep=fep,
        interp=interp,
        s2v_interp=s2v_interp,
        resamp=resamp,
        nvoxhp=nvoxhp,
        initrand=initrand,
        ff=ff,
        repol=repol,
        ol_nstd=ol_nstd,
        ol_nvox=ol_nvox,
        ol_type=ol_type,
        ol_pos=ol_pos,
        ol_sqr=ol_sqr,
        estimate_move_by_susceptibility=estimate_move_by_susceptibility,
        mbs_niter=mbs_niter,
        mbs_lambda=mbs_lambda,
        mbs_ksp=mbs_ksp,
        dont_sep_offs_move=dont_sep_offs_move,
        dont_peas=dont_peas,
        data_is_shelled=data_is_shelled,
        verbose=verbose,
    )
    return eddy_cuda9_1_execute(params, execution)


__all__ = [
    "EDDY_CUDA9_1_METADATA",
    "EddyCuda91Outputs",
    "EddyCuda91Parameters",
    "eddy_cuda9_1",
    "eddy_cuda9_1_params",
]
