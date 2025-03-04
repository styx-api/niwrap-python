# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_ROBUST_REGISTER_METADATA = Metadata(
    id="fe2158f128fa82fc3156d764c03ca5f6fec2935c.boutiques",
    name="mri_robust_register",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriRobustRegisterParameters = typing.TypedDict('MriRobustRegisterParameters', {
    "__STYX_TYPE__": typing.Literal["mri_robust_register"],
    "movable_volume": InputPathType,
    "target_volume": InputPathType,
    "output_registration": str,
    "outlier_sensitivity": typing.NotRequired[float | None],
    "satit": bool,
    "mapped_movable": typing.NotRequired[str | None],
    "mapped_movable_hdr": typing.NotRequired[str | None],
    "weights": typing.NotRequired[str | None],
    "oneminus_w": bool,
    "iscale": bool,
    "iscale_only": bool,
    "iscale_out": typing.NotRequired[str | None],
    "iscale_in": typing.NotRequired[str | None],
    "trans_only": bool,
    "affine": bool,
    "ixform": typing.NotRequired[str | None],
    "init_orient": bool,
    "no_init": bool,
    "vox2vox": bool,
    "cost": typing.NotRequired[str | None],
    "ent_radius": typing.NotRequired[float | None],
    "ent_correction": bool,
    "ent_ball": bool,
    "ent_mov": typing.NotRequired[str | None],
    "powell_tolerance": typing.NotRequired[float | None],
    "sobel": bool,
    "no_sym": bool,
    "maximum_iterations": typing.NotRequired[float | None],
    "ent_dst": typing.NotRequired[str | None],
    "high_iter": typing.NotRequired[float | None],
    "eps_iteration": typing.NotRequired[float | None],
    "no_multiscale": bool,
    "max_size": typing.NotRequired[float | None],
    "min_size": typing.NotRequired[float | None],
    "w_limit": typing.NotRequired[float | None],
    "sub_sample": typing.NotRequired[float | None],
    "float_type": bool,
    "white_bg_mov": bool,
    "white_bg_dst": bool,
    "uchar": bool,
    "mask_mov": typing.NotRequired[InputPathType | None],
    "mask_dst": typing.NotRequired[InputPathType | None],
    "half_mov": typing.NotRequired[str | None],
    "half_dst": typing.NotRequired[str | None],
    "half_weights": typing.NotRequired[str | None],
    "half_mov_lta": typing.NotRequired[str | None],
    "half_dst_lta": typing.NotRequired[str | None],
    "debug": bool,
    "verbose": typing.NotRequired[float | None],
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
        "mri_robust_register": mri_robust_register_cargs,
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
        "mri_robust_register": mri_robust_register_outputs,
    }.get(t)


class MriRobustRegisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_robust_register(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reg_output: OutputPathType
    """Registration output file containing the transformation from movable to
    destination."""
    mapped_output: OutputPathType | None
    """Movable volume mapped and resampled at destination."""
    mapped_hdr_output: OutputPathType | None
    """Movable volume aligned to destination (header only)."""
    weights_output_file: OutputPathType | None
    """Weights indicating outlier probabilities in destination space."""
    iscale_out_file: OutputPathType | None
    """Output text file containing the intensity scale value."""
    half_mov_file: OutputPathType | None
    """Half-way movable volume resampled."""
    half_dst_file: OutputPathType | None
    """Half-way destination volume resampled."""
    half_weights_file: OutputPathType | None
    """Half-way weights resampled in halfway space."""
    half_mov_lta_file: OutputPathType | None
    """Transform output from movable to half-way space."""
    half_dst_lta_file: OutputPathType | None
    """Transform output from destination to half-way space."""
    ent_mov_file: OutputPathType | None
    """Movable entropy image for ROBENT cost function."""
    ent_dst_file: OutputPathType | None
    """Target entropy image for ROBENT cost function."""


def mri_robust_register_params(
    movable_volume: InputPathType,
    target_volume: InputPathType,
    output_registration: str,
    outlier_sensitivity: float | None = None,
    satit: bool = False,
    mapped_movable: str | None = None,
    mapped_movable_hdr: str | None = None,
    weights: str | None = None,
    oneminus_w: bool = False,
    iscale: bool = False,
    iscale_only: bool = False,
    iscale_out: str | None = None,
    iscale_in: str | None = None,
    trans_only: bool = False,
    affine: bool = False,
    ixform: str | None = None,
    init_orient: bool = False,
    no_init: bool = False,
    vox2vox: bool = False,
    cost: str | None = None,
    ent_radius: float | None = None,
    ent_correction: bool = False,
    ent_ball: bool = False,
    ent_mov: str | None = None,
    powell_tolerance: float | None = None,
    sobel: bool = False,
    no_sym: bool = False,
    maximum_iterations: float | None = None,
    ent_dst: str | None = None,
    high_iter: float | None = None,
    eps_iteration: float | None = None,
    no_multiscale: bool = False,
    max_size: float | None = None,
    min_size: float | None = None,
    w_limit: float | None = None,
    sub_sample: float | None = None,
    float_type: bool = False,
    white_bg_mov: bool = False,
    white_bg_dst: bool = False,
    uchar: bool = False,
    mask_mov: InputPathType | None = None,
    mask_dst: InputPathType | None = None,
    half_mov: str | None = None,
    half_dst: str | None = None,
    half_weights: str | None = None,
    half_mov_lta: str | None = None,
    half_dst_lta: str | None = None,
    debug: bool = False,
    verbose: float | None = None,
) -> MriRobustRegisterParameters:
    """
    Build parameters.
    
    Args:
        movable_volume: Input movable volume to be aligned to target.
        target_volume: Input target volume.
        output_registration: Output registration (transform from mov to dst).
        outlier_sensitivity: Set outlier sensitivity manually for robust cost\
            functions. Higher values mean less sensitivity.
        satit: Auto-detect good sensitivity for robust cost functions.
        mapped_movable: Output image: movable mapped and resampled at\
            destination.
        mapped_movable_hdr: Output image: movable aligned to destination (no\
            resampling, only adjusting header vox2ras).
        weights: Output weights (outlier probabilities) in destination space\
            (0=regular,1=outlier).
        oneminus_w: Weights (outlier) map will be inverted (0=outlier), as in\
            earlier versions.
        iscale: Estimate intensity scale factor.
        iscale_only: Only perform intensity scaling (no transformation).
        iscale_out: Output text file for iscale value.
        iscale_in: Initial input text file for iscale value.
        trans_only: Find 3 parameter translation only.
        affine: Find 12 parameter affine transform.
        ixform: Use initial transform LTA on source.
        init_orient: Use moments for orientation initialization.
        no_init: Skip automatic transform initialization.
        vox2vox: Output VOX2VOX LTA file.
        cost: Set cost function for registration.
        ent_radius: With ROBENT: specify box radius for entropy computation.
        ent_correction: With ROBENT: use better entropy computation that works\
            on smaller boxes.
        ent_ball: With ROBENT: use ball around voxel instead of box.
        ent_mov: With ROBENT: write movable entropy image.
        powell_tolerance: With MI, NMI etc: set Powell tolerance.
        sobel: Register Sobel magnitude images.
        no_sym: Do not map to half way space.
        maximum_iterations: Maximum number of iterations on each resolution.
        ent_dst: With ROBENT: write target entropy image.
        high_iter: Maximum number of iterations on highest resolution.
        eps_iteration: Stop iterations when transform update falls below\
            specified RMS distance.
        no_multiscale: Process highest resolution only (no multiscale).
        max_size: Specify largest voxel dimension for gaussian pyramid.
        min_size: Specify smallest voxel dimension for gaussian pyramid.
        w_limit: (Expert) sets maximal outlier limit for --satit.
        sub_sample: Subsample if dimension is greater than the specified value\
            on all axes.
        float_type: Convert images to float internally.
        white_bg_mov: Assume white background in MOV for padding.
        white_bg_dst: Assume white background in DST for padding.
        uchar: Convert inputs to UCHAR with rescale and histogram cropping.
        mask_mov: Mask movable image with mask file.
        mask_dst: Mask destination image with mask file.
        half_mov: Outputs half-way movable (resampled in halfway space).
        half_dst: Outputs half-way destination (resampled in halfway space).
        half_weights: Outputs half-way weights (resampled in halfway space).
        half_mov_lta: Outputs transform from movable to half-way space.
        half_dst_lta: Outputs transform from destination to half-way space.
        debug: Show debug output.
        verbose: Verbosity level: 0 (quiet), 1 (normal), 2 (detail).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_robust_register",
        "movable_volume": movable_volume,
        "target_volume": target_volume,
        "output_registration": output_registration,
        "satit": satit,
        "oneminus_w": oneminus_w,
        "iscale": iscale,
        "iscale_only": iscale_only,
        "trans_only": trans_only,
        "affine": affine,
        "init_orient": init_orient,
        "no_init": no_init,
        "vox2vox": vox2vox,
        "ent_correction": ent_correction,
        "ent_ball": ent_ball,
        "sobel": sobel,
        "no_sym": no_sym,
        "no_multiscale": no_multiscale,
        "float_type": float_type,
        "white_bg_mov": white_bg_mov,
        "white_bg_dst": white_bg_dst,
        "uchar": uchar,
        "debug": debug,
    }
    if outlier_sensitivity is not None:
        params["outlier_sensitivity"] = outlier_sensitivity
    if mapped_movable is not None:
        params["mapped_movable"] = mapped_movable
    if mapped_movable_hdr is not None:
        params["mapped_movable_hdr"] = mapped_movable_hdr
    if weights is not None:
        params["weights"] = weights
    if iscale_out is not None:
        params["iscale_out"] = iscale_out
    if iscale_in is not None:
        params["iscale_in"] = iscale_in
    if ixform is not None:
        params["ixform"] = ixform
    if cost is not None:
        params["cost"] = cost
    if ent_radius is not None:
        params["ent_radius"] = ent_radius
    if ent_mov is not None:
        params["ent_mov"] = ent_mov
    if powell_tolerance is not None:
        params["powell_tolerance"] = powell_tolerance
    if maximum_iterations is not None:
        params["maximum_iterations"] = maximum_iterations
    if ent_dst is not None:
        params["ent_dst"] = ent_dst
    if high_iter is not None:
        params["high_iter"] = high_iter
    if eps_iteration is not None:
        params["eps_iteration"] = eps_iteration
    if max_size is not None:
        params["max_size"] = max_size
    if min_size is not None:
        params["min_size"] = min_size
    if w_limit is not None:
        params["w_limit"] = w_limit
    if sub_sample is not None:
        params["sub_sample"] = sub_sample
    if mask_mov is not None:
        params["mask_mov"] = mask_mov
    if mask_dst is not None:
        params["mask_dst"] = mask_dst
    if half_mov is not None:
        params["half_mov"] = half_mov
    if half_dst is not None:
        params["half_dst"] = half_dst
    if half_weights is not None:
        params["half_weights"] = half_weights
    if half_mov_lta is not None:
        params["half_mov_lta"] = half_mov_lta
    if half_dst_lta is not None:
        params["half_dst_lta"] = half_dst_lta
    if verbose is not None:
        params["verbose"] = verbose
    return params


def mri_robust_register_cargs(
    params: MriRobustRegisterParameters,
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
    cargs.append("mri_robust_register")
    cargs.extend([
        "-mov",
        execution.input_file(params.get("movable_volume"))
    ])
    cargs.extend([
        "-dst",
        execution.input_file(params.get("target_volume"))
    ])
    cargs.extend([
        "-lta",
        params.get("output_registration")
    ])
    if params.get("outlier_sensitivity") is not None:
        cargs.extend([
            "--sat",
            str(params.get("outlier_sensitivity"))
        ])
    if params.get("satit"):
        cargs.append("--satit")
    if params.get("mapped_movable") is not None:
        cargs.extend([
            "--mapmov",
            params.get("mapped_movable")
        ])
    if params.get("mapped_movable_hdr") is not None:
        cargs.extend([
            "--mapmovhdr",
            params.get("mapped_movable_hdr")
        ])
    if params.get("weights") is not None:
        cargs.extend([
            "--weights",
            params.get("weights")
        ])
    if params.get("oneminus_w"):
        cargs.append("--oneminusw")
    if params.get("iscale"):
        cargs.append("--iscale")
    if params.get("iscale_only"):
        cargs.append("--iscaleonly")
    if params.get("iscale_out") is not None:
        cargs.extend([
            "--iscaleout",
            params.get("iscale_out")
        ])
    if params.get("iscale_in") is not None:
        cargs.extend([
            "--iscalein",
            params.get("iscale_in")
        ])
    if params.get("trans_only"):
        cargs.append("--transonly")
    if params.get("affine"):
        cargs.append("--affine")
    if params.get("ixform") is not None:
        cargs.extend([
            "--ixform",
            params.get("ixform")
        ])
    if params.get("init_orient"):
        cargs.append("--initorient")
    if params.get("no_init"):
        cargs.append("--noinit")
    if params.get("vox2vox"):
        cargs.append("--vox2vox")
    if params.get("cost") is not None:
        cargs.extend([
            "--cost",
            params.get("cost")
        ])
    if params.get("ent_radius") is not None:
        cargs.extend([
            "--entradius",
            str(params.get("ent_radius"))
        ])
    if params.get("ent_correction"):
        cargs.append("--entcorrection")
    if params.get("ent_ball"):
        cargs.append("--entball")
    if params.get("ent_mov") is not None:
        cargs.extend([
            "--entmov",
            params.get("ent_mov")
        ])
    if params.get("powell_tolerance") is not None:
        cargs.extend([
            "--powelltol",
            str(params.get("powell_tolerance"))
        ])
    if params.get("sobel"):
        cargs.append("--sobel")
    if params.get("no_sym"):
        cargs.append("--nosym")
    if params.get("maximum_iterations") is not None:
        cargs.extend([
            "--maxit",
            str(params.get("maximum_iterations"))
        ])
    if params.get("ent_dst") is not None:
        cargs.extend([
            "--entdst",
            params.get("ent_dst")
        ])
    if params.get("high_iter") is not None:
        cargs.extend([
            "--highit",
            str(params.get("high_iter"))
        ])
    if params.get("eps_iteration") is not None:
        cargs.extend([
            "--epsit",
            str(params.get("eps_iteration"))
        ])
    if params.get("no_multiscale"):
        cargs.append("--nomulti")
    if params.get("max_size") is not None:
        cargs.extend([
            "--maxsize",
            str(params.get("max_size"))
        ])
    if params.get("min_size") is not None:
        cargs.extend([
            "--minsize",
            str(params.get("min_size"))
        ])
    if params.get("w_limit") is not None:
        cargs.extend([
            "--wlimit",
            str(params.get("w_limit"))
        ])
    if params.get("sub_sample") is not None:
        cargs.extend([
            "--subsample",
            str(params.get("sub_sample"))
        ])
    if params.get("float_type"):
        cargs.append("--floattype")
    if params.get("white_bg_mov"):
        cargs.append("--whitebgmov")
    if params.get("white_bg_dst"):
        cargs.append("--whitebgdst")
    if params.get("uchar"):
        cargs.append("--uchar")
    if params.get("mask_mov") is not None:
        cargs.extend([
            "--maskmov",
            execution.input_file(params.get("mask_mov"))
        ])
    if params.get("mask_dst") is not None:
        cargs.extend([
            "--maskdst",
            execution.input_file(params.get("mask_dst"))
        ])
    if params.get("half_mov") is not None:
        cargs.extend([
            "--halfmov",
            params.get("half_mov")
        ])
    if params.get("half_dst") is not None:
        cargs.extend([
            "--halfdst",
            params.get("half_dst")
        ])
    if params.get("half_weights") is not None:
        cargs.extend([
            "--halfweights",
            params.get("half_weights")
        ])
    if params.get("half_mov_lta") is not None:
        cargs.extend([
            "--halfmovlta",
            params.get("half_mov_lta")
        ])
    if params.get("half_dst_lta") is not None:
        cargs.extend([
            "--halfdstlta",
            params.get("half_dst_lta")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("verbose") is not None:
        cargs.extend([
            "--verbose",
            str(params.get("verbose"))
        ])
    return cargs


def mri_robust_register_outputs(
    params: MriRobustRegisterParameters,
    execution: Execution,
) -> MriRobustRegisterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriRobustRegisterOutputs(
        root=execution.output_file("."),
        reg_output=execution.output_file(params.get("output_registration")),
        mapped_output=execution.output_file(params.get("mapped_movable")) if (params.get("mapped_movable") is not None) else None,
        mapped_hdr_output=execution.output_file(params.get("mapped_movable_hdr")) if (params.get("mapped_movable_hdr") is not None) else None,
        weights_output_file=execution.output_file(params.get("weights")) if (params.get("weights") is not None) else None,
        iscale_out_file=execution.output_file(params.get("iscale_out")) if (params.get("iscale_out") is not None) else None,
        half_mov_file=execution.output_file(params.get("half_mov")) if (params.get("half_mov") is not None) else None,
        half_dst_file=execution.output_file(params.get("half_dst")) if (params.get("half_dst") is not None) else None,
        half_weights_file=execution.output_file(params.get("half_weights")) if (params.get("half_weights") is not None) else None,
        half_mov_lta_file=execution.output_file(params.get("half_mov_lta")) if (params.get("half_mov_lta") is not None) else None,
        half_dst_lta_file=execution.output_file(params.get("half_dst_lta")) if (params.get("half_dst_lta") is not None) else None,
        ent_mov_file=execution.output_file(params.get("ent_mov")) if (params.get("ent_mov") is not None) else None,
        ent_dst_file=execution.output_file(params.get("ent_dst")) if (params.get("ent_dst") is not None) else None,
    )
    return ret


def mri_robust_register_execute(
    params: MriRobustRegisterParameters,
    execution: Execution,
) -> MriRobustRegisterOutputs:
    """
    Inverse consistent registration of two volumes using robust and standard cost
    functions.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriRobustRegisterOutputs`).
    """
    params = execution.params(params)
    cargs = mri_robust_register_cargs(params, execution)
    ret = mri_robust_register_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_robust_register(
    movable_volume: InputPathType,
    target_volume: InputPathType,
    output_registration: str,
    outlier_sensitivity: float | None = None,
    satit: bool = False,
    mapped_movable: str | None = None,
    mapped_movable_hdr: str | None = None,
    weights: str | None = None,
    oneminus_w: bool = False,
    iscale: bool = False,
    iscale_only: bool = False,
    iscale_out: str | None = None,
    iscale_in: str | None = None,
    trans_only: bool = False,
    affine: bool = False,
    ixform: str | None = None,
    init_orient: bool = False,
    no_init: bool = False,
    vox2vox: bool = False,
    cost: str | None = None,
    ent_radius: float | None = None,
    ent_correction: bool = False,
    ent_ball: bool = False,
    ent_mov: str | None = None,
    powell_tolerance: float | None = None,
    sobel: bool = False,
    no_sym: bool = False,
    maximum_iterations: float | None = None,
    ent_dst: str | None = None,
    high_iter: float | None = None,
    eps_iteration: float | None = None,
    no_multiscale: bool = False,
    max_size: float | None = None,
    min_size: float | None = None,
    w_limit: float | None = None,
    sub_sample: float | None = None,
    float_type: bool = False,
    white_bg_mov: bool = False,
    white_bg_dst: bool = False,
    uchar: bool = False,
    mask_mov: InputPathType | None = None,
    mask_dst: InputPathType | None = None,
    half_mov: str | None = None,
    half_dst: str | None = None,
    half_weights: str | None = None,
    half_mov_lta: str | None = None,
    half_dst_lta: str | None = None,
    debug: bool = False,
    verbose: float | None = None,
    runner: Runner | None = None,
) -> MriRobustRegisterOutputs:
    """
    Inverse consistent registration of two volumes using robust and standard cost
    functions.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        movable_volume: Input movable volume to be aligned to target.
        target_volume: Input target volume.
        output_registration: Output registration (transform from mov to dst).
        outlier_sensitivity: Set outlier sensitivity manually for robust cost\
            functions. Higher values mean less sensitivity.
        satit: Auto-detect good sensitivity for robust cost functions.
        mapped_movable: Output image: movable mapped and resampled at\
            destination.
        mapped_movable_hdr: Output image: movable aligned to destination (no\
            resampling, only adjusting header vox2ras).
        weights: Output weights (outlier probabilities) in destination space\
            (0=regular,1=outlier).
        oneminus_w: Weights (outlier) map will be inverted (0=outlier), as in\
            earlier versions.
        iscale: Estimate intensity scale factor.
        iscale_only: Only perform intensity scaling (no transformation).
        iscale_out: Output text file for iscale value.
        iscale_in: Initial input text file for iscale value.
        trans_only: Find 3 parameter translation only.
        affine: Find 12 parameter affine transform.
        ixform: Use initial transform LTA on source.
        init_orient: Use moments for orientation initialization.
        no_init: Skip automatic transform initialization.
        vox2vox: Output VOX2VOX LTA file.
        cost: Set cost function for registration.
        ent_radius: With ROBENT: specify box radius for entropy computation.
        ent_correction: With ROBENT: use better entropy computation that works\
            on smaller boxes.
        ent_ball: With ROBENT: use ball around voxel instead of box.
        ent_mov: With ROBENT: write movable entropy image.
        powell_tolerance: With MI, NMI etc: set Powell tolerance.
        sobel: Register Sobel magnitude images.
        no_sym: Do not map to half way space.
        maximum_iterations: Maximum number of iterations on each resolution.
        ent_dst: With ROBENT: write target entropy image.
        high_iter: Maximum number of iterations on highest resolution.
        eps_iteration: Stop iterations when transform update falls below\
            specified RMS distance.
        no_multiscale: Process highest resolution only (no multiscale).
        max_size: Specify largest voxel dimension for gaussian pyramid.
        min_size: Specify smallest voxel dimension for gaussian pyramid.
        w_limit: (Expert) sets maximal outlier limit for --satit.
        sub_sample: Subsample if dimension is greater than the specified value\
            on all axes.
        float_type: Convert images to float internally.
        white_bg_mov: Assume white background in MOV for padding.
        white_bg_dst: Assume white background in DST for padding.
        uchar: Convert inputs to UCHAR with rescale and histogram cropping.
        mask_mov: Mask movable image with mask file.
        mask_dst: Mask destination image with mask file.
        half_mov: Outputs half-way movable (resampled in halfway space).
        half_dst: Outputs half-way destination (resampled in halfway space).
        half_weights: Outputs half-way weights (resampled in halfway space).
        half_mov_lta: Outputs transform from movable to half-way space.
        half_dst_lta: Outputs transform from destination to half-way space.
        debug: Show debug output.
        verbose: Verbosity level: 0 (quiet), 1 (normal), 2 (detail).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRobustRegisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_ROBUST_REGISTER_METADATA)
    params = mri_robust_register_params(
        movable_volume=movable_volume,
        target_volume=target_volume,
        output_registration=output_registration,
        outlier_sensitivity=outlier_sensitivity,
        satit=satit,
        mapped_movable=mapped_movable,
        mapped_movable_hdr=mapped_movable_hdr,
        weights=weights,
        oneminus_w=oneminus_w,
        iscale=iscale,
        iscale_only=iscale_only,
        iscale_out=iscale_out,
        iscale_in=iscale_in,
        trans_only=trans_only,
        affine=affine,
        ixform=ixform,
        init_orient=init_orient,
        no_init=no_init,
        vox2vox=vox2vox,
        cost=cost,
        ent_radius=ent_radius,
        ent_correction=ent_correction,
        ent_ball=ent_ball,
        ent_mov=ent_mov,
        powell_tolerance=powell_tolerance,
        sobel=sobel,
        no_sym=no_sym,
        maximum_iterations=maximum_iterations,
        ent_dst=ent_dst,
        high_iter=high_iter,
        eps_iteration=eps_iteration,
        no_multiscale=no_multiscale,
        max_size=max_size,
        min_size=min_size,
        w_limit=w_limit,
        sub_sample=sub_sample,
        float_type=float_type,
        white_bg_mov=white_bg_mov,
        white_bg_dst=white_bg_dst,
        uchar=uchar,
        mask_mov=mask_mov,
        mask_dst=mask_dst,
        half_mov=half_mov,
        half_dst=half_dst,
        half_weights=half_weights,
        half_mov_lta=half_mov_lta,
        half_dst_lta=half_dst_lta,
        debug=debug,
        verbose=verbose,
    )
    return mri_robust_register_execute(params, execution)


__all__ = [
    "MRI_ROBUST_REGISTER_METADATA",
    "MriRobustRegisterOutputs",
    "MriRobustRegisterParameters",
    "mri_robust_register",
    "mri_robust_register_params",
]
